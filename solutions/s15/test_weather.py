import pytest
from fastapi.testclient import TestClient

import main
from weather import parse

SAMPLE = {
    "hourly": {
        "time": ["2026-10-30T00:00", "2026-10-30T01:00"],
        "temperature_2m": [12.5, 11.9],
        "precipitation_probability": [10, 60],
    }
}


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setattr(main, "fetch_today", lambda city="서울": parse(SAMPLE))
    return TestClient(main.app)


def test_city(client: TestClient) -> None:
    response = client.get("/city/부산")
    assert response.status_code == 200
    assert "오늘 부산 날씨" in response.text
    assert "가장 추운 때 01:00" in response.text


def test_unknown_city(client: TestClient) -> None:
    assert client.get("/city/뉴욕").status_code == 404


def test_min_rain(client: TestClient) -> None:
    assert [h["time"] for h in client.get("/api/today?min_rain=50").json()] == ["01:00"]

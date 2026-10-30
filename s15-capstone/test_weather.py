import pytest
from fastapi.testclient import TestClient

import main
from weather import Hour, parse

SAMPLE = {
    "hourly": {
        "time": ["2026-10-30T00:00", "2026-10-30T01:00"],
        "temperature_2m": [12.5, 11.9],
        "precipitation_probability": [10, 60],
    }
}


def test_parse() -> None:
    hours = parse(SAMPLE)
    assert hours == [Hour("00:00", 12.5, 10), Hour("01:00", 11.9, 60)]


def test_home(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "fetch_today", lambda: parse(SAMPLE))
    response = TestClient(main.app).get("/")
    assert response.status_code == 200
    assert "가장 따뜻한 때 00:00" in response.text

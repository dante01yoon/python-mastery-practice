from dataclasses import dataclass
from typing import Any

import httpx

URL = "https://api.open-meteo.com/v1/forecast"
CITIES = {
    "서울": (37.5665, 126.978),
    "부산": (35.1796, 129.0756),
    "제주": (33.4996, 126.5312),
}


@dataclass
class Hour:
    time: str
    temp: float
    rain: int


def parse(data: dict[str, Any]) -> list[Hour]:
    hourly = data["hourly"]
    times = hourly["time"]
    temps = hourly["temperature_2m"]
    rains = hourly["precipitation_probability"]
    return [Hour(t[11:16], temp, rain) for t, temp, rain in zip(times, temps, rains)]


def fetch_today(city: str = "서울") -> list[Hour]:
    lat, lon = CITIES[city]
    params: dict[str, str | float | int] = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation_probability",
        "timezone": "Asia/Seoul",
        "forecast_days": 1,
    }
    return parse(httpx.get(URL, params=params, timeout=10).json())

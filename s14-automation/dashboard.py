from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import httpx
from openpyxl import Workbook
from rich.console import Console
from rich.table import Table

CITIES = {
    "서울": (37.5665, 126.978),
    "부산": (35.1796, 129.0756),
    "제주": (33.4996, 126.5312),
}


def temperature(city: str) -> float:
    lat, lon = CITIES[city]
    params = {"latitude": lat, "longitude": lon, "current": "temperature_2m"}
    url = "https://api.open-meteo.com/v1/forecast"
    return httpx.get(url, params=params, timeout=10).json()["current"]["temperature_2m"]


def usd_rates() -> dict[str, float]:
    url = "https://api.frankfurter.dev/v1/latest"
    params = {"base": "USD", "symbols": "KRW,JPY,EUR"}
    return httpx.get(url, params=params, timeout=10).json()["rates"]


with ThreadPoolExecutor() as pool:
    temps = list(pool.map(temperature, CITIES))

rows = [(f"{city} 기온", f"{t}°C") for city, t in zip(CITIES, temps)]
rows += [(f"1달러 → {code}", f"{rate:,.2f}") for code, rate in usd_rates().items()]

table = Table(title=f"오늘의 대시보드 · {datetime.now():%H:%M}")
table.add_column("항목")
table.add_column("값", justify="right")
for name, value in rows:
    table.add_row(name, value)
Console().print(table)

wb = Workbook()
ws = wb.active
ws.append(["항목", "값"])
for row in rows:
    ws.append(list(row))
wb.save("dashboard.xlsx")
print("dashboard.xlsx에 저장했어요")

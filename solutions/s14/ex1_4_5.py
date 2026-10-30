import re

import httpx
from bs4 import BeautifulSoup

text = "회의는 2026-10-29, 발표는 2026-11-05에 해요."
print(re.findall(r"\d{4}-\d{2}-\d{2}", text))
print(re.sub(r"\d{4}-(\d{2})-(\d{2})", lambda m: f"{int(m[1])}월 {int(m[2])}일", text))

params = {
    "latitude": 37.5665,
    "longitude": 126.978,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "Asia/Seoul",
    "forecast_days": 2,
}
daily = httpx.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10).json()["daily"]
print(f"내일 {daily['time'][1]} 최고 {daily['temperature_2m_max'][1]}°C 최저 {daily['temperature_2m_min'][1]}°C")

soup = BeautifulSoup(httpx.get("https://books.toscrape.com/", timeout=10).text, "html.parser")
for book in soup.select("article.product_pod"):
    price = float(book.select_one(".price_color").text.lstrip("£"))
    if price < 20:
        print(price, book.h3.a["title"])

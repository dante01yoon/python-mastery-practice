import csv
import time
from urllib.robotparser import RobotFileParser

import httpx
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/catalogue/"
robots = RobotFileParser("https://books.toscrape.com/robots.txt")
robots.read()
rows = []
for page in range(1, 6):
    url = f"{BASE}page-{page}.html"
    if not robots.can_fetch("*", url):
        break
    soup = BeautifulSoup(httpx.get(url, timeout=10).text, "html.parser")
    for book in soup.select("article.product_pod"):
        price = float(book.select_one(".price_color").text.lstrip("£Â"))
        if price > 50:
            rows.append([book.h3.a["title"], price])
    time.sleep(1)
with open("expensive.csv", "w", newline="", encoding="utf-8-sig") as f:
    csv.writer(f).writerows([["title", "price"], *rows])
print(len(rows))

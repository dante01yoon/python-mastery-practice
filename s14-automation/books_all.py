import csv
import time
from urllib.robotparser import RobotFileParser

import httpx
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/catalogue/"
robots = RobotFileParser("https://books.toscrape.com/robots.txt")
robots.read()
print(robots.can_fetch("*", BASE + "page-2.html"))

rows = []
for page in range(1, 4):
    html = httpx.get(f"{BASE}page-{page}.html", timeout=10).text
    soup = BeautifulSoup(html, "html.parser")
    for book in soup.select("article.product_pod"):
        rows.append([page, book.h3.a["title"], book.select_one(".price_color").text])
    time.sleep(1)
print(len(rows), rows[0])

with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["page", "title", "price"])
    writer.writerows(rows)
print("저장했어요")

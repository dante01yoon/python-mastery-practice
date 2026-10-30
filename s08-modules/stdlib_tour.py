from collections import Counter
from datetime import date, timedelta
from statistics import mean

today = date(2026, 10, 29)
print(today + timedelta(days=100))
print(today.strftime("%Y년 %m월 %d일"))

words = "사과 배 사과 귤 사과 배".split()
counts = Counter(words)
print(counts.most_common(2))

sales = [120, 95, 130, 110]
print(mean(sales))

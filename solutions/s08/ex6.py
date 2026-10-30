from datetime import date, timedelta

today = date(2026, 11, 1)
print((date(2027, 1, 1) - today).days)
print((today + timedelta(days=30)).strftime("%Y년 %m월 %d일"))

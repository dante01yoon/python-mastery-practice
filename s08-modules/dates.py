from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

exam = date(2026, 12, 25)
day = date(2026, 11, 1)
left = exam - day
print(left.days)
print(day + timedelta(days=100))

meet = datetime(2026, 11, 3, 14, 30)
print(meet.strftime("%Y년 %m월 %d일 %H시 %M분"))
start = datetime.strptime("2026-11-03 09:00", "%Y-%m-%d %H:%M")
print(meet - start)

seoul = datetime(2026, 11, 3, 14, 30, tzinfo=ZoneInfo("Asia/Seoul"))
london = seoul.astimezone(ZoneInfo("Europe/London"))
print(seoul)
print(london)

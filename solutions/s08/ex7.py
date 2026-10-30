from datetime import datetime
from zoneinfo import ZoneInfo

seoul = datetime(2026, 11, 3, 9, 0, tzinfo=ZoneInfo("Asia/Seoul"))
print(seoul.astimezone(ZoneInfo("Europe/London")))
print(seoul.astimezone(ZoneInfo("Asia/Tokyo")))

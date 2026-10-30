from datetime import date, timedelta


def days_later(start: date, days: int) -> date:
    return start + timedelta(days=days)

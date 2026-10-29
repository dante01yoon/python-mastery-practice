import csv
from pathlib import Path

path = Path(__file__).parent.parent.parent / "s07-files" / "spending.csv"
with open(path, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        if int(row["금액"]) >= 10000:
            print(row["날짜"], row["항목"], row["금액"])

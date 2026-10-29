import csv

total = 0
by_item = {}
with open("spending.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        amount = int(row["금액"])
        total += amount
        by_item[row["항목"]] = by_item.get(row["항목"], 0) + amount

print(f"합계: {total:,}원")
for item, amount in by_item.items():
    print(f"{item}: {amount:,}원")

with open("summary.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["항목", "합계"])
    for item, amount in by_item.items():
        writer.writerow([item, amount])

files = ["report.csv", "photo.png", "sales.csv", "memo.txt"]

csv_files = [f for f in files if f.endswith(".csv")]
print(csv_files)

squares = [n * n for n in range(1, 6)]
print(squares)

prices = {"사과": 1500, "우유": 2800}
with_tax = {name: int(price * 1.1) for name, price in prices.items()}
print(with_tax)

lengths = {len(f) for f in files}
print(lengths)

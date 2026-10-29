from pathlib import Path

base = Path("data")
base.mkdir(exist_ok=True)

memo = base / "memo.txt"
memo.write_text("pathlib로 쓴 메모\n", encoding="utf-8")

print(memo)
print(memo.exists())
print(memo.read_text(encoding="utf-8").strip())
print(memo.name, memo.suffix)

for p in sorted(base.glob("*.txt")):
    print("찾음:", p.name)

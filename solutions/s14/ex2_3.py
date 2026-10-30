import shutil
import tempfile
from collections import Counter
from pathlib import Path

from openpyxl import Workbook

KINDS = {
    "문서": [".pdf", ".docx", ".txt"],
    "사진": [".jpg", ".png"],
    "표": [".xlsx", ".csv"],
    "압축": [".zip"],
}

# 2번: 원본을 건드리지 않게 임시 폴더에 복사해서 정리한다
src = Path(__file__).parent.parent.parent / "s14-automation" / "downloads"
folder = Path(tempfile.mkdtemp()) / "downloads"
shutil.copytree(src, folder)
for file in sorted(folder.iterdir()):
    for kind, suffixes in KINDS.items():
        if file.is_file() and file.suffix in suffixes:
            (folder / kind).mkdir(exist_ok=True)
            shutil.move(file, folder / kind / file.name)
for sub in sorted(folder.iterdir()):
    print(sub.name, len(list(sub.iterdir())), "개")

# 3번
sales = [("커피", 4500), ("케이크", 6800), ("커피", 4500)]
totals = Counter()
for item, price in sales:
    totals[item] += price
wb = Workbook()
ws = wb.active
ws.title = "상품별 합계"
ws.append(["상품", "합계"])
for item, total in totals.items():
    ws.append([item, total])
out = Path(tempfile.mkdtemp()) / "summary.xlsx"
wb.save(out)
print(dict(totals), "→", out.name)

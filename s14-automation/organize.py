import shutil
from datetime import date
from pathlib import Path

KINDS = {
    "문서": [".pdf", ".docx", ".txt"],
    "사진": [".jpg", ".png"],
    "표": [".xlsx", ".csv"],
}

folder = Path("downloads")
for file in sorted(folder.iterdir()):
    if not file.is_file():
        continue
    for kind, suffixes in KINDS.items():
        if file.suffix in suffixes:
            target = folder / kind
            target.mkdir(exist_ok=True)
            shutil.move(file, target / file.name)
            print(f"{file.name} → {kind}")

backup = shutil.make_archive(f"backup-{date.today()}", "zip", folder)
print("백업:", Path(backup).name)

from pathlib import Path

from PIL import Image

out = Path("small")
out.mkdir(exist_ok=True)
for path in sorted(Path("photos").glob("*.*")):
    with Image.open(path) as img:
        before = img.size
        img.thumbnail((800, 800))
        img.convert("RGB").save(out / f"{path.stem}.jpg", quality=85)
        print(path.name, before, "→", img.size)

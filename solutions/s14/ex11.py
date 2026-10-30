from pathlib import Path

from PIL import Image

out = Path("small400")
out.mkdir(exist_ok=True)
for path in sorted(Path("photos").glob("*.*")):
    with Image.open(path) as img:
        img.thumbnail((400, 400))
        img.save(out / f"{path.stem}.png")  # png는 RGBA도 그대로 저장된다
        print(path.name, "→", img.size, img.mode)

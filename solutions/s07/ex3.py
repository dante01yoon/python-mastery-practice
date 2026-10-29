from pathlib import Path

backup = Path("backup")
backup.mkdir(exist_ok=True)
(backup / "todo-copy.txt").write_text(Path("todo.txt").read_text(encoding="utf-8"), encoding="utf-8")
print(sorted(p.name for p in backup.iterdir()))

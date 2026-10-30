import json
from pathlib import Path


def save_notes(path: Path, notes: list[str]) -> None:
    path.write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")


def load_notes(path: Path) -> list[str]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))

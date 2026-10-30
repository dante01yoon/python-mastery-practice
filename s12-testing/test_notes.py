from pathlib import Path

import pytest

from notes import load_notes, save_notes


@pytest.fixture
def sample() -> list[str]:
    return ["장보기", "운동"]


def test_save_and_load(tmp_path: Path, sample: list[str]) -> None:
    file = tmp_path / "notes.json"
    save_notes(file, sample)
    assert load_notes(file) == sample


def test_load_missing(tmp_path: Path) -> None:
    assert load_notes(tmp_path / "없음.json") == []

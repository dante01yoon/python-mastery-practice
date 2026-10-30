from pathlib import Path

import pytest


def reverse(text: str) -> str:
    return text[::-1]


def is_even(n: int) -> bool:
    return n % 2 == 0


def test_reverse() -> None:
    assert reverse("abc") == "cba"
    assert reverse("") == ""


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, True), (1, False), (2, True), (-3, False), (10, True)],
)
def test_is_even(n: int, expected: bool) -> None:
    assert is_even(n) is expected


def test_int_error() -> None:
    with pytest.raises(ValueError):
        int("abc")


def test_file_roundtrip(tmp_path: Path) -> None:
    file = tmp_path / "memo.txt"
    file.write_text("안녕", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "안녕"

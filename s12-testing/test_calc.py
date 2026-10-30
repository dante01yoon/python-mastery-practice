import pytest

from calc import average, grade


def test_average() -> None:
    assert average([80, 90, 70]) == 80


def test_grade() -> None:
    assert grade(95) == "A"
    assert grade(85) == "B"


def test_grade_perfect() -> None:
    assert grade(100) == "A+"


def test_average_empty() -> None:
    with pytest.raises(ZeroDivisionError):
        average([])


@pytest.mark.parametrize(
    ("score", "expected"),
    [(100, "A+"), (95, "A"), (90, "A"), (89, "B"), (80, "B"), (79, "C")],
)
def test_grade_table(score: int, expected: str) -> None:
    assert grade(score) == expected

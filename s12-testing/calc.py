def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def grade(score: int) -> str:
    if score == 100:
        return "A+"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    return "C"

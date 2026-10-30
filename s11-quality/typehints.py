def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


print(average([80, 90, 70]))


def find_age(ages: dict[str, int], name: str) -> int | None:
    return ages.get(name)


ages = {"민지": 29, "준호": 34}
age = find_age(ages, "서연")
if age is None:
    print("없는 사람이에요")
else:
    print(age + 1)


type Scores = dict[str, list[int]]


def best(scores: Scores) -> str:
    return max(scores, key=lambda name: average(scores[name]))


print(best({"민지": [90, 85], "준호": [70, 100]}))

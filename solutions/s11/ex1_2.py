def no_scores(scores: dict[str, list[int]]) -> list[str]:
    return [name for name, values in scores.items() if not values]


def first_negative(nums: list[int]) -> int | None:
    for n in nums:
        if n < 0:
            return n
    return None


print(no_scores({"민지": [90], "준호": [], "서연": []}))

found = first_negative([3, 8, -2, -7])
if found is None:
    print("음수가 없어요")
else:
    print(found * 10)

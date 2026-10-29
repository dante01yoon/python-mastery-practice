def evens(numbers: list) -> list:
    """짝수만 담은 새 리스트를 돌려준다."""
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


print(evens([1, 2, 3, 4, 5, 6]))

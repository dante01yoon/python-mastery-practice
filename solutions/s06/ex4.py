def check_age(age: int) -> int:
    if age < 0:
        raise ValueError("나이는 0 이상")
    return age


try:
    check_age(-3)
except ValueError as e:
    print("잘못된 나이:", e)

while True:
    text = input("나이를 숫자로: ")
    try:
        age = int(text)
    except ValueError:
        print("숫자로만 적어 주세요")
    else:
        print(f"내년엔 {age + 1}살")
        break


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로는 나눌 수 없어요")
        return None
    finally:
        print("계산 끝")


print(divide(10, 2))
print(divide(10, 0))

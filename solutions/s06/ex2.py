try:
    a = int(input("첫 숫자: "))
    b = int(input("둘째 숫자: "))
    print(a / b)
except ValueError:
    print("숫자로 적어 주세요")
except ZeroDivisionError:
    print("0으로는 못 나눠요")

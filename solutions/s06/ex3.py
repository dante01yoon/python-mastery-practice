fruits = ["사과", "배", "귤"]
try:
    print(fruits[int(input("번호: "))])
except IndexError:
    print("0~2 중에 골라 주세요")
except ValueError:
    print("숫자로 적어 주세요")

# 리스트: 수업에서 한 줄씩 친 코드
fruits = ["사과", "바나나", "포도"]
print(fruits[0], fruits[-1])
print(len(fruits))

fruits.append("딸기")
fruits[1] = "망고"
print(fruits)

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:2], numbers[3:])
print("포도" in fruits)

name = "python"
name[0] = "P"  # 문자열은 바꿀 수 없어서 TypeError가 난다

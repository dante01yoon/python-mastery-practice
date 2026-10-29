# 반복문: 수업에서 한 줄씩 친 코드
for i in range(1, 4):
    print(i, "번째 인사")

fruits = ["사과", "망고", "포도"]
for fruit in fruits:
    print(fruit)

count = 3
while count > 0:
    print(count)
    count = count - 1
print("발사!")

while True:
    word = input("단어 (q는 종료): ")
    if word == "q":
        break
    print(word * 2)

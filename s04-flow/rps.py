# 미니 프로젝트 4: 가위바위보
import random

choices = ["가위", "바위", "보"]
wins = {"가위": "보", "바위": "가위", "보": "바위"}  # 왼쪽이 오른쪽을 이긴다

while True:
    me = input("가위/바위/보 (q는 종료): ")
    if me == "q":
        break
    if me not in choices:
        print("다시 입력하세요")
        continue
    com = random.choice(choices)
    print(f"컴퓨터: {com}")
    if me == com:
        print("비겼어요")
    elif wins[me] == com:
        print("이겼어요!")
    else:
        print("졌어요")

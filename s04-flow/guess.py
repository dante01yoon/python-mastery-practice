# 미니 프로젝트 3: 숫자 맞히기(UP/DOWN)
import random

random.seed(7)  # 연습할 때 매번 같은 수가 나오게 — 다 만들면 이 줄을 지운다
secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("1~100 숫자: "))
    tries += 1
    if guess < secret:
        print("UP")
    elif guess > secret:
        print("DOWN")
    else:
        print(f"정답! {tries}번 만에 맞혔어요")
        break

price = int(input("가격: "))
count = int(input("개수: "))
total = round(price * count * 1.1)  # 1.1은 소수라 오차가 생길 수 있어 반올림
print(f"총액 {total}원")

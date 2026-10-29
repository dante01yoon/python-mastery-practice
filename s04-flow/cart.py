menu = {"사과": 1500, "우유": 2800, "빵": 3200}
cart = []

while True:
    item = input("담을 물건 (끝은 q): ")
    if item == "q":
        break
    if item not in menu:
        print("없는 물건이에요")
        continue
    cart.append(item)
    print(f"{item} 담음")

total = 0
for item in cart:
    total += menu[item]
print(f"장바구니: {cart}")
print(f"합계: {total:,}원")

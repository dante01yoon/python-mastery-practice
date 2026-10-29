class NotEnoughMoney(Exception):
    """잔액이 모자랄 때 쓰는 예외."""


def withdraw(balance: int, amount: int) -> int:
    if amount <= 0:
        raise ValueError("0보다 큰 금액만 돼요")
    if amount > balance:
        raise NotEnoughMoney(f"잔액 {balance}원, 요청 {amount}원")
    return balance - amount


print(withdraw(10000, 3000))

try:
    withdraw(10000, 50000)
except NotEnoughMoney as e:
    print("출금 실패:", e)

try:
    withdraw(10000, -500)
except ValueError as e:
    print("잘못된 금액:", e)

class NotEnoughMoney(Exception):
    """잔액이 모자랄 때 쓰는 예외."""


def read_amount(prompt: str) -> int:
    """0보다 큰 숫자를 받을 때까지 다시 묻는다."""
    while True:
        try:
            amount = int(input(prompt))
        except ValueError:
            print("숫자로만 적어 주세요")
            continue
        if amount <= 0:
            print("0보다 큰 금액만 돼요")
            continue
        return amount


def withdraw(balance: int, amount: int) -> int:
    if amount > balance:
        raise NotEnoughMoney(f"잔액이 {balance:,}원뿐이에요")
    return balance - amount


balance = 0
while True:
    print(f"잔액: {balance:,}원")
    menu = input("1 입금  2 출금  3 끝: ")
    if menu == "1":
        balance += read_amount("입금할 금액: ")
    elif menu == "2":
        try:
            balance = withdraw(balance, read_amount("출금할 금액: "))
        except NotEnoughMoney as e:
            print("출금 실패:", e)
    elif menu == "3":
        print("안녕히 가세요")
        break
    else:
        print("1, 2, 3 중에 골라 주세요")

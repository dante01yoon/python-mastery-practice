class Account:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("잔액이 모자라요")
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, owner: str, balance: int = 0):
        super().__init__(owner, balance)

    def add_interest(self, rate: float) -> None:
        self.balance += int(self.balance * rate)


acc = SavingsAccount("민지", 10000)
acc.deposit(5000)
acc.add_interest(0.03)
print(acc.balance)
try:
    acc.withdraw(100000)
except ValueError as e:
    print(e)

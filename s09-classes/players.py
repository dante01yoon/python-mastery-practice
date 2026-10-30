class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def wants_card(self) -> bool:
        return input(f"{self.name}, 한 장 더? (y/n) ") == "y"


class Dealer(Player):
    """딜러는 규칙대로만 움직인다: 16 이하면 무조건 한 장 더."""

    def __init__(self):
        super().__init__("딜러")

    def wants_card(self) -> bool:
        return self.score <= 16


dealer = Dealer()
dealer.score = 15
print(dealer.name, dealer.wants_card())
dealer.score = 18
print(dealer.name, dealer.wants_card())
print(isinstance(dealer, Player))

class Card:
    """트럼프 카드 한 장."""

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def show(self) -> str:
        return self.suit + self.rank


ace = Card("♠", "A")
king = Card("♥", "K")
print(ace.show(), king.show())
print(ace.rank, king.suit)

import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return self.suit + self.rank


class Deck:
    """카드 52장 한 벌."""

    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()


random.seed(7)
deck = Deck()
print(len(deck))
deck.shuffle()
card = deck.draw()
print(card)
print(len(deck))

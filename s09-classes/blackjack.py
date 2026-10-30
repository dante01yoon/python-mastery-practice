import random
from dataclasses import dataclass

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


@dataclass
class Card:
    suit: str
    rank: str

    def __str__(self) -> str:
        return self.suit + self.rank


class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards: list[Card] = []

    def add(self, card: Card) -> None:
        self.cards.append(card)

    @property
    def value(self) -> int:
        total, aces = 0, 0
        for card in self.cards:
            if card.rank == "A":
                total, aces = total + 11, aces + 1
            elif card.rank in ("J", "Q", "K"):
                total += 10
            else:
                total += int(card.rank)
        while total > 21 and aces:
            total, aces = total - 10, aces - 1
        return total

    def __str__(self) -> str:
        return " ".join(str(c) for c in self.cards) + f"  ({self.value})"


def play() -> None:
    deck = Deck()
    me, dealer = Hand(), Hand()
    for _ in range(2):
        me.add(deck.draw())
        dealer.add(deck.draw())
    print("딜러:", dealer.cards[0], "??")
    while me.value < 21:
        print("나:", me)
        if input("한 장 더? (y/n) ") != "y":
            break
        me.add(deck.draw())
    print("나:", me)
    if me.value > 21:
        print("버스트! 졌어요")
        return
    while dealer.value <= 16:
        dealer.add(deck.draw())
    print("딜러:", dealer)
    if dealer.value > 21 or me.value > dealer.value:
        print("이겼어요!")
    elif me.value == dealer.value:
        print("비겼어요")
    else:
        print("졌어요")


random.seed(4)
play()

from dataclasses import dataclass


@dataclass
class Card:
    suit: str
    rank: str


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


print(Card("♠", "A"))
hand = Hand()
hand.add(Card("♠", "A"))
hand.add(Card("♥", "K"))
print(hand.value)
hand.add(Card("♦", "5"))
print(hand.value)

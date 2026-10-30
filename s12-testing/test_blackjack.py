from blackjack import Card, Deck, Hand


def test_ace_and_king() -> None:
    hand = Hand()
    hand.add(Card("♠", "A"))
    hand.add(Card("♥", "K"))
    assert hand.value == 21


def test_two_aces() -> None:
    hand = Hand()
    for rank in ["A", "A", "9"]:
        hand.add(Card("♣", rank))
    assert hand.value == 21


def test_bust() -> None:
    hand = Hand()
    for rank in ["K", "Q", "5"]:
        hand.add(Card("♦", rank))
    assert hand.value > 21


def test_deck_draw() -> None:
    deck = Deck()
    assert len(deck.cards) == 52
    deck.draw()
    assert len(deck.cards) == 51

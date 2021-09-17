import random


class Deck:
    """
    A container for Cards.
    Empty to begin with.
    Functionality to
    add a list of cards,
    remove a specified number of card
    and randomize the order of the cards.
    """

    def __init__(self):
        self._cards = []

    def add_cards(self, cards):
        self._cards.extend(cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def remove_cards(self, number):
        cards_to_remove = self._cards[:number]
        del self._cards[:number]
        return cards_to_remove

import random

class Deck():
    """
    A container for Cards.
    Empty to begin with.
    Includes functionality to 
    add cards and shuffle cards.
    """
    def __init__(self):
        self._cards = []
    
    def add_cards(self, cards):
        self._cards.extend(cards)

    def shuffle(self):
        random.shuffle(self._cards)
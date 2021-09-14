class Deck():
    """
    A container for Cards.
    Empty to begin with.
    """
    def __init__(self):
        self._cards = []
    
    def add_cards(self, cards):
        self._cards.extend(cards)

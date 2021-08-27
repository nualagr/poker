class Deck():
    """
    A container for Cards.
    Empty to begin with.
    """
    def __init__(self):
        self.cards = []
    
    def add_cards(self, cards):
        self.cards.extend(cards)

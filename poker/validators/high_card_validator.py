class HighCardValidator:
    """
    This class knows what makes up a valid High Card
    It knows its name.
    It knows what cards to return for that High Card.
    """

    def __init__(self, cards):
        self.cards = cards
        self.name = "High Card"

    def is_valid(self):
        return len(self.cards) >= 2

    def valid_cards(self):
        # As we know the list is sorted
        # Therefore - return a list of the last card
        # which will be the highest card
        return self.cards[-1:]

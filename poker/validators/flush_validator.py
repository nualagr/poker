class FlushValidator:
    def __init__(self, cards):
        self.cards = cards
        self.name = "Flush"

    def is_valid(self):
        if len(self._suits_that_occur_five_or_more_times) == 1:
            return True

    def valid_cards(self):
        cards = [
            card
            for card in self.cards
            if card.suit in self._suits_that_occur_five_or_more_times.keys()
        ]
        return cards[-5:]

    @property
    def _suits_that_occur_five_or_more_times(self):
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }  # {'Diamonds': 6}

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            # If the card suit exists in the dict, nothing will change
            # if the card suit does not exist in the dict, it will be
            # added with a count of zero
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts

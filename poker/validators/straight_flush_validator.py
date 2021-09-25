from poker.validators import FiveCardRanksInARowValidator


class StraightFlushValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"

    def is_valid(self):
        # [[3, 4, 5, 6, 7]]
        for five_cards in self._collections_of_five_straight_cards_in_a_row:
            # Remove duplicate suits using set
            unique_suits_in_next_five_cards = {card.suit for card in five_cards}
            if len(unique_suits_in_next_five_cards) == 1:
                return True

        return False

    def valid_cards(self):
        # Return the highest straight flush within self.cards
        # if more than one exists
        # [[3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
        return self._straight_flush_card_batches[-1]

    @property
    def _straight_flush_card_batches(self):
        return [
            # return the five card batch
            five_cards
            # for every batch which has a confirmed straight
            for five_cards in self._collections_of_five_straight_cards_in_a_row
            # IF, after removing duplicates, only one suit remains in the set
            if len({card.suit for card in five_cards}) == 1
        ]

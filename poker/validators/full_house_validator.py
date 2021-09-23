from poker.validators import ThreeOfAKindValidator, PairValidator


class FullHouseValidator:
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        if (
            ThreeOfAKindValidator(cards=self.cards).is_valid()
            and PairValidator(cards=self.cards).is_valid()
        ):
            return True

    def valid_cards(self):
        pair_cards = PairValidator(cards=self.cards).valid_cards()
        three_of_a_kind_cards = ThreeOfAKindValidator(cards=self.cards).valid_cards()
        all_cards = pair_cards + three_of_a_kind_cards
        all_cards.sort()
        return all_cards

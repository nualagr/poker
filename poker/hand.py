from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator,
)


class Hand:
    def __init__(self):
        """
        Create a Hand object with
        an empty cards list.
        """
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    @property
    def _rank_validations_from_best_to_worst(self):
        return (
            # Instantiate each Validator Object.
            # Provide a reference to the 'is_valid' method on each
            # that can then be invoked, by the Hand 'best_rank' method
            # to return a Boolean
            ("Royal Flush", RoyalFlushValidator(cards=self.cards).is_valid),
            ("Straight Flush", StraightFlushValidator(cards=self.cards).is_valid),
            ("Four of a Kind", FourOfAKindValidator(cards=self.cards).is_valid),
            ("Full House", FullHouseValidator(cards=self.cards).is_valid),
            ("Flush", FlushValidator(cards=self.cards).is_valid),
            ("Straight", StraightValidator(cards=self.cards).is_valid),
            ("Three of a Kind", ThreeOfAKindValidator(cards=self.cards).is_valid),
            ("Two Pair", TwoPairValidator(cards=self.cards).is_valid),
            ("Pair", PairValidator(cards=self.cards).is_valid),
            ("High Card", HighCardValidator(cards=self.cards).is_valid),
            ("No Cards", NoCardsValidator(cards=self.cards).is_valid),
        )

    def best_rank(self):
        for rank in self._rank_validations_from_best_to_worst:
            # Unpack the tuple into variables
            name, validator_func = rank
            # Invoke the method/function to return a Boolean
            if validator_func() == True:
                return name

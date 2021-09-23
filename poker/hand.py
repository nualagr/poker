from poker.validators import (
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
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind", self._four_of_a_kind),
            ("Four of a Kind", self._four_of_a_kind),
            # Instantiate each Validator Object.
            # Provide a reference to the 'is_valid' method on each
            # that can then be invoked, by the Hand 'best_rank' method
            # to return a Boolean
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

    def _royal_flush(self):
        is_straight_flush = self._straight_flush()
        if not is_straight_flush:
            return False

        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal

    def _straight_flush(self):
        return (
            FlushValidator(cards=self.cards).is_valid()
            and StraightValidator(cards=self.cards).is_valid()
        )

    def _four_of_a_kind(self):
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            # Only if the card rank does not already exist in the dict
            # will it be added to the dict with a count of zero
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

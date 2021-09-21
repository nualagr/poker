from poker.validators import PairValidator, HighCardValidator, NoCardsValidator


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
            ("Full House", self._full_house),
            ("Flush", self._flush),
            ("Straight", self._straight),
            ("Three of a Kind", self._three_of_a_kind),
            ("Two Pair", self._two_pair),
            ("Pair", PairValidator(cards=self.cards).is_valid),
            # Instantiate a HighCardValidator Object.
            # Provide a reference to the method on the Validator Class
            # that can then be invoked, by best_rank, to return a Boolean
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
        return self._flush() and self._straight()

    def _four_of_a_kind(self):
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1

    def _full_house(self):
        if self._three_of_a_kind() and PairValidator(cards=self.cards).is_valid():
            return True

    def _flush(self):
        suits_that_occur_five_or_more_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }
        if len(suits_that_occur_five_or_more_times) == 1:
            return True

    def _straight(self):
        """
        Check that the current hand has at least 5 cards.
        Convert cards list into a list of the cards' rank_index.
        Use range() to generate a strictly-increasing list
        from the first card.rank_index to the last, increment
        the latter by one. Compare the two lists.
        Return True if the two lists are equal.
        """
        if len(self.cards) < 5:
            return False
        rank_indexes = [card.rank_index for card in self.cards]
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1] + 1
        straight_consecutive_indexes = list(range(starting_rank_index, last_rank_index))
        if rank_indexes == straight_consecutive_indexes:
            return True

    def _three_of_a_kind(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1

    def _two_pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

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

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            # Only if the card rank does not already exist in the dict
            # will it be added to the dict with a count of zero
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

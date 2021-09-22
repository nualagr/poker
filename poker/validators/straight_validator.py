class StraightValidator:
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        """
        Iterate over self.cards in batches of five.
        Determine if the each card's rank-index
        within the current batch is strictly increasing
        by one each time. If so, store the batch of cards in
        a list.
        If more than one straight exists in self.cards,
        return the higher of the two straights.
        """
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1

    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_a_row[-1]

    @property
    def _collections_of_five_straight_cards_in_a_row(self):
        index = 0
        final_index = len(self.cards) - 1
        collections_of_five_straight_cards_in_a_row = []

        # Keep iterating as long as index + 4
        # is still within the bounds of the
        # indexes in the self.cards list.
        while index + 4 <= final_index:
            # Account for the upperbound being exclusive in list slicing syntax
            next_five_cards = self.cards[index : index + 5]

            # Isolate the rank indexes to pass to _every_element_increasing_by() helper function
            next_five_rank_indices = [card.rank_index for card in next_five_cards]

            if self._every_element_increasing_by_1(next_five_rank_indices):
                collections_of_five_straight_cards_in_a_row.append(next_five_cards)

            index += 1

        return collections_of_five_straight_cards_in_a_row

    def _every_element_increasing_by_1(self, rank_indexes):
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1] + 1
        straight_consecutive_indexes = list(range(starting_rank_index, last_rank_index))
        if rank_indexes == straight_consecutive_indexes:
            return True

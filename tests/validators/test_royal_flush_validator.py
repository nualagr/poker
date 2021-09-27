import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator


class RoyalFlushValidatorTest(unittest.TestCase):
    def test_confirms_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank="9", suit="Hearts"),
            Card(rank="10", suit="Hearts"),
            Card(rank="Jack", suit="Hearts"),
            Card(rank="Queen", suit="Hearts"),
            Card(rank="King", suit="Hearts"),
            Card(rank="Ace", suit="Diamonds"),
        ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(validator.is_valid(), False)

    def test_confirms_that_cards_do_have_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank="9", suit="Clubs"),
            Card(rank="10", suit="Hearts"),
            Card(rank="Jack", suit="Hearts"),
            Card(rank="Queen", suit="Hearts"),
            Card(rank="King", suit="Hearts"),
            Card(rank="Ace", suit="Hearts"),
            Card(rank="Ace", suit="Spades"),
        ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        ten = Card(rank="10", suit="Hearts")
        jack = Card(rank="Jack", suit="Hearts")
        queen = Card(rank="Queen", suit="Hearts")
        king = Card(rank="King", suit="Hearts")
        ace = Card(rank="Ace", suit="Hearts")

        cards = [
            Card(rank="9", suit="Clubs"),
            ten,
            jack,
            queen,
            king,
            ace,
            Card(rank="Ace", suit="Spades"),
        ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten,
                jack,
                queen,
                king,
                ace,
            ],
        )

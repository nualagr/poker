import unittest

from poker.card import Card
from poker.validators import StraightValidator


class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven = Card(rank="7", suit="Spades")
        self.eight = Card(rank="8", suit="Hearts")
        self.nine = Card(rank="9", suit="Hearts")
        self.ten = Card(rank="10", suit="Clubs")
        self.jack = Card(rank="Jack", suit="Diamonds")
        self.queen = Card(rank="Queen", suit="Clubs")
        self.ace = Card(rank="Ace", suit="Hearts")

        self.cards = [
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack,
            self.queen,
            self.ace,
        ]

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [Card(rank="Jack", suit="Clubs"), Card(rank="Queen", suit="Hearts")]

        validator = StraightValidator(cards=cards)

        self.assertEqual(validator.is_valid(), False)

    def test_determines_if_there_are_five_cards_in_a_row(self):

        validator = StraightValidator(cards=self.cards)
        self.assertEqual(validator.is_valid(), True)

    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(cards=self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.eight,
                self.nine,
                self.ten,
                self.jack,
                self.queen,
            ],
        )

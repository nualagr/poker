import unittest

from poker.card import Card
from poker.validators import FlushValidator


class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_diamonds = Card(rank="2", suit="Diamonds")
        self.five_of_diamonds = Card(rank="5", suit="Diamonds")
        self.eight_of_diamonds = Card(rank="8", suit="Diamonds")
        self.nine_of_diamonds = Card(rank="9", suit="Diamonds")
        self.ten_of_diamonds = Card(rank="10", suit="Diamonds")
        self.ace_of_diamonds = Card(rank="Ace", suit="Diamonds")

        self.cards = [
            Card(rank="2", suit="Clubs"),
            self.two_of_diamonds,
            self.five_of_diamonds,
            self.eight_of_diamonds,
            self.nine_of_diamonds,
            self.ten_of_diamonds,
            self.ace_of_diamonds,
        ]

    def test_validates_that_five_cards_of_same_suit_exist_in_collection(self):
        validator = FlushValidator(cards=self.cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_the_five_highest_cards_with_same_suit_from_collection(self):
        validator = FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_diamonds,
                self.eight_of_diamonds,
                self.nine_of_diamonds,
                self.ten_of_diamonds,
                self.ace_of_diamonds,
            ],
        )

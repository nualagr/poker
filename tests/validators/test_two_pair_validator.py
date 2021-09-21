import unittest

from poker.card import Card
from poker.validators import TwoPairValidator


class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_diamonds = Card(rank="3", suit="Diamonds")
        self.nine_of_diamonds = Card(rank="9", suit="Diamonds")
        self.nine_of_spades = Card(rank="9", suit="Spades")
        self.jack_of_diamonds = Card(rank="Jack", suit="Diamonds")
        self.jack_of_hearts = Card(rank="Jack", suit="Hearts")

        self.cards = [
            self.three_of_diamonds,
            self.nine_of_diamonds,
            self.nine_of_spades,
            self.jack_of_diamonds,
            self.jack_of_hearts,
        ]

    def test_validates_that_cards_have_at_least_two_pairs_of_same_rank(self):
        validator = TwoPairValidator(cards=self.cards)
        self.assertEqual(validator.is_valid(), True)

    def test_returns_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(cards=self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.nine_of_diamonds,
                self.nine_of_spades,
                self.jack_of_diamonds,
                self.jack_of_hearts,
            ],
        )

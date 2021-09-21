import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator


class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.ace_of_spades = Card(rank="Ace", suit="Spades")
        self.king_of_clubs = Card(rank="King", suit="Clubs")
        self.two_of_diamonds = Card(rank="2", suit="Diamonds")
        self.two_of_clubs = Card(rank="2", suit="Clubs")
        self.two_of_hearts = Card(rank="2", suit="Hearts")

        self.cards = [
            self.ace_of_spades,
            self.king_of_clubs,
            self.two_of_clubs,
            self.two_of_diamonds,
            self.two_of_hearts,
        ]

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        validator = ThreeOfAKindValidator(cards=self.cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_three_of_a_kind_from_collection(self):
        validator = ThreeOfAKindValidator(cards=self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.two_of_clubs,
                self.two_of_diamonds,
                self.two_of_hearts,
            ],
        )

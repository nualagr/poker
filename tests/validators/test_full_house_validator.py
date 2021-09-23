import unittest

from poker.card import Card
from poker.validators import FullHouseValidator


class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.six_of_diamonds = Card(rank="6", suit="Diamonds")
        self.six_of_hearts = Card(rank="6", suit="Hearts")
        self.six_of_spades = Card(rank="6", suit="Spades")
        self.king_of_clubs = Card(rank="King", suit="Clubs")
        self.king_of_hearts = Card(rank="King", suit="Hearts")

        self.cards = [
            Card(rank="2", suit="Diamonds"),
            self.six_of_diamonds,
            self.six_of_hearts,
            self.six_of_spades,
            self.king_of_clubs,
            self.king_of_hearts,
            Card(rank="Ace", suit="Spades"),
        ]

    def test_validates_cards_have_two_of_the_same_rank_and_three_of_another_rank(self):
        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_pair_and_three_of_a_kind_from_collection(self):
        validator = FullHouseValidator(cards=self.cards)
        self.assertEqual(
            validator.valid_cards(),
            [
                self.six_of_diamonds,
                self.six_of_hearts,
                self.six_of_spades,
                self.king_of_clubs,
                self.king_of_hearts,
            ],
        )

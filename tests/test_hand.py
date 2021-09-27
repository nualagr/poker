import unittest
from poker.card import Card
from poker.hand import Hand


class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [Card(rank="Ace", suit="Clubs"), Card(rank="3", suit="Spades")]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(repr(hand), "3 of Spades, Ace of Clubs")

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        six_of_clubs = Card(rank="6", suit="Clubs")
        cards = [ace_of_spades, six_of_clubs]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(hand.cards, [six_of_clubs, ace_of_spades])

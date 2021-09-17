import unittest
from unittest.mock import patch

import random

from poker.card import Card
from poker.deck import Deck

class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck._cards,
            []
        )
    
    def test_adds_cards_to_its_collection(self):
        card = Card("Ace", "Spades")
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(
            deck._cards,
            [card]
        )
    
    @patch('random.shuffle')
    # Need to feed in a second argument to the test
    # to represent the mock_shuffle function that patch 
    # will generate
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "2", suit = "Diamonds")
        ]

        deck = Deck()
        deck.add_cards(cards)

        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)
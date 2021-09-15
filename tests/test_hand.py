import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        six_of_clubs = Card(rank = "6", suit = "Clubs")
        cards = [
            ace_of_spades,
            six_of_clubs            
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.cards,
            [
                six_of_clubs, 
                ace_of_spades
            ]
        )
    
    def test_figures_out_high_card_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )
    
    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "2", suit = "Diamonds"),
            Card(rank = "2", suit = "Clubs"),
            Card(rank = "5", suit = "Hearts")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )
    
    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "2", suit = "Diamonds"),
            Card(rank = "2", suit = "Clubs"),
            Card(rank = "2", suit = "Hearts")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )
    
    def test_figures_out_straight_is_best_rank(self):
        cards = [
            Card(rank = "6", suit = "Spades"),
            Card(rank = "7", suit = "Clubs"),
            Card(rank = "8", suit = "Diamonds"),
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "10", suit = "Hearts")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )
    
    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Hearts")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )
    
    def test_figures_out_flush_is_best_rank(self):
        cards = [
            Card(rank = rank, suit = "Diamonds")
            for rank in ["2", "5", "8", "10", "Ace"]
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )
    
    def test_figures_out_full_house_is_best_rank(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "6", suit = "Spades"),
            Card(rank = "6", suit = "Diamonds"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "King", suit = "Hearts")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "Full House"
        ) 
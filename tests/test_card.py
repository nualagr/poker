import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_card_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")
    
    def test_card_has_suit(self):
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")
    
    def test_knows_its_rank_index(self):
        card = Card(rank = "Ace", suit = "Diamonds")
        self.assertEqual(card.rank_index, 12)

    def test_has_string_representation_with_rank_and_suit(self):
        card = Card(rank = "3", suit = "Spades")
        self.assertEqual(str(card), "3 of Spades")
    
    def test_has_technical_representation(self):
        card = Card(rank = "10", suit = "Diamonds")
        self.assertEqual(repr(card), "Card(rank = '10', suit = 'Diamonds')")
    
    def test_card_has_four_possible_suit_options(self):
        self.assertEqual(
            # For constant data use uppercase
            Card.SUITS, 
            ("Clubs", "Diamonds", "Hearts", "Spades")
        )
    
    def test_card_has_thirteen_possible_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            (
                "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "Jack", "Queen", "King", "Ace"
            )
        )
    
    def test_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Clubs")
    
    def test_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "4", suit = "Jokers")
    
    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)

        self.assertEqual(
            cards[0],
            Card(rank = "2", suit = "Clubs")
        )

        self.assertEqual(
            cards[-1],
            Card(rank = "Ace", suit = "Spades")
        )

    def test_asserts_true_if_two_cards_have_the_same_rank_and_suit(self):
        self.assertEqual(
            Card(rank = "5", suit = "Diamonds"),
            Card(rank = "5", suit = "Diamonds")
        )
    def test_card_can_sort_itself_with_another_one(self):
        queen_of_spades = Card(rank = "Queen", suit = "Spades")
        king_of_spades = Card(rank = "King", suit = "Spades")
        evaluation = queen_of_spades < king_of_spades
        self.assertEqual(
            evaluation,
            True,
            "The sort algorithm is not sorting the lower card first."
        ) 
  
    def test_sorts_cards(self):
        two_of_spades = Card(rank = "2", suit = "Spades")
        five_of_diamonds = Card(rank = "5", suit = "Diamonds")
        five_of_hearts = Card(rank = "5", suit = "Hearts")
        eight_of_hearts = Card(rank = "8", suit = "Hearts")
        ace_of_clubs = Card(rank = "Ace", suit = "Spades")

        unsorted_cards = [
            five_of_diamonds,
            two_of_spades,
            five_of_hearts, 
            ace_of_clubs,
            eight_of_hearts
        ]

        # sort mutates the list in place
        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards, 
            [
            two_of_spades,
            five_of_diamonds,
            five_of_hearts,
            eight_of_hearts, 
            ace_of_clubs
            ]
        )
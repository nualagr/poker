import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.hand import Hand
from poker.player import Player


class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name="Barry", hand=hand)
        self.assertEqual(player.name, "Barry")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"

        player = Player(name="Barry", hand=mock_hand)

        self.assertEqual(player.best_hand(), "Straight Flush")

        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()

        player = Player(name="Ken", hand=mock_hand)

        cards = [Card(rank="Ace", suit="Spades"), Card(rank="Queen", suit="Diamonds")]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_once_with(cards)

    def test_decides_to_continue_or_drop_out_of_game(self):
        player = Player(name="Sharon", hand=Hand())

        self.assertEqual(player.wants_to_fold(), False)

    def test_is_sorted_by_best_hand(self):
        mock_hand_1 = MagicMock()
        mock_hand_1.best_rank.return_value = (
            0,
            "Royal Flush",
            [
                Card(rank="10", suit="Diamonds"),
                Card(rank="Jack", suit="Diamonds"),
                Card(rank="Queen", suit="Diamonds"),
                Card(rank="King", suit="Diamonds"),
                Card(rank="Ace", suit="Diamonds"),
            ],
        )
        mock_hand_2 = MagicMock()
        mock_hand_2.best_rank.return_value = (
            7,
            "Two Pair",
            [
                Card(rank="Jack", suit="Clubs"),
                Card(rank="Jack", suit="Spades"),
            ],
        )

        player1 = Player(name="Beatrice", hand=mock_hand_1)
        player2 = Player(name="Bernadette", hand=mock_hand_2)

        players = [player1, player2]

        self.assertEqual(max(players), player1)

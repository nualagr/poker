import unittest
from unittest.mock import MagicMock

from poker.game import Game

class GameTest(unittest.TestCase):
    def test_stores_deck_and_players(self):
        deck = MagicMock()
        players = [
            MagicMock(),
            MagicMock()
        ]

        game = Game(
            deck = deck,
            players = players
        )

        self.assertEqual(
            game.deck,
            deck
        )

        self.assertEqual(
            game.players,
            players
        )
    
    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]

        game = Game(
            deck = mock_deck,
            players = players
        )

        game.play()
        mock_deck.shuffle.assert_called_once()
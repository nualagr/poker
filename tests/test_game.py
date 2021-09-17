import unittest
from unittest.mock import MagicMock, call

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
    
    def test_deals_two_initial_cards_from_deck_to_each_player(self):
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

        # Test that remove_cards has been called twice
        # Test that remove_cards was called with the argument 2 each time
        mock_deck.remove_cards.assert_has_calls(
            [call(2), call(2)]
        )       
import unittest
from unittest.mock import MagicMock, call

from poker.card import Card
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
        first_two_cards = [
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "9", suit = "Diamonds")
        ]
        second_two_cards = [
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "10", suit = "Clubs")
        ]

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [first_two_cards, second_two_cards]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [mock_player1, mock_player2]

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
        
        mock_player1.add_cards.assert_called_with(first_two_cards),
        mock_player2.add_cards.assert_called_with(second_two_cards)
import unittest
from unittest.mock import MagicMock, call

from poker.card import Card
from poker.game import Game


class GameTest(unittest.TestCase):
    def setUp(self):
        self.first_two_cards = [
            Card(rank="3", suit="Hearts"),
            Card(rank="9", suit="Diamonds"),
        ]
        self.second_two_cards = [
            Card(rank="Jack", suit="Clubs"),
            Card(rank="10", suit="Clubs"),
        ]
        self.flop_cards = [
            Card(rank="2", suit="Diamonds"),
            Card(rank="4", suit="Hearts"),
            Card(rank="10", suit="Spades"),
        ]
        self.turn_card = [Card(rank="Ace", suit="Clubs")]
        self.river_card = [Card(rank="10", suit="Hearts")]

    def test_stores_deck_and_players(self):
        deck = MagicMock()
        players = [MagicMock(), MagicMock()]

        game = Game(deck=deck, players=players)

        self.assertEqual(game.deck, deck)

        self.assertEqual(game.players, players)

    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()

        players = [MagicMock(), MagicMock()]

        game = Game(deck=mock_deck, players=players)

        game.play()
        mock_deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_from_deck_to_each_player(self):
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.second_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card,
        ]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [mock_player1, mock_player2]

        game = Game(deck=mock_deck, players=players)

        game.play()

        # Test that remove_cards has been called twice
        # Test that remove_cards was called with the argument 2 each time
        mock_deck.remove_cards.assert_has_calls([call(2), call(2)])

        # Test that, at some point in the execution,
        # add_cards was called with the first two cards drawn from the deck
        mock_player1.add_cards.assert_has_calls([call(self.first_two_cards)])
        mock_player2.add_cards.assert_has_calls([call(self.second_two_cards)])

    def test_removes_player_if_not_willing_to_make_bet(self):
        mock_deck = MagicMock()
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = True
        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False

        players = [mock_player1, mock_player2]

        game = Game(deck=mock_deck, players=players)
        game.play()

        self.assertEqual(game.players, [mock_player2])

    def test_deals_each_player_3_flop_1_turn_and_1_river_card(self):
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = False
        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False
        players = [mock_player1, mock_player2]

        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.second_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card,
        ]

        game = Game(deck=mock_deck, players=players)
        game.play()
        # Test that we made a call to the Deck with the remove_cards method
        # with an argument of 3
        mock_deck.remove_cards.assert_has_calls([call(3), call(1), call(1)])
        # Test that we've called the 'add_cards' method on each player
        # with all three community calls
        calls = [call(self.flop_cards), call(self.turn_card), call(self.river_card)]

        for player in players:
            player.add_cards.assert_has_calls(calls)

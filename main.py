# Launching point for the program
# It sits at the top level
# It is a sibling file with the 'poker' directory
from poker.card import Card
from poker.deck import Deck
from poker.game import Game
from poker.hand import Hand
from poker.player import Player

# When initially testing:
# card1 = Card(rank = "2", suit = "Spades")
# card2 = Card(rank = "Ace", suit = "Hearts")
# In the Python3 Interpreter:
# from main import card1, card2
# This provides access these cards in the namespace

deck = Deck()

cards = Card.create_standard_52_cards()

deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name="Ben", hand=hand1)
player2 = Player(name="Bobby", hand=hand2)
players = [player1, player2]

game = Game(deck=deck, players=players)
game.play()
# In the Python3 Interpreter:
# from main import deck, cards, game, hand1, hand2, player1, player2

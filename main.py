# Launching point for the program
# It sits at the top level
# It is a sibling file with the 'poker' directory
from poker.card import Card
from poker.deck import Deck

# When initially testing:
# card1 = Card(rank = "2", suit = "Spades")
# card2 = Card(rank = "Ace", suit = "Hearts")
# In the Python3 Interpreter:
# from main import card1, card2
# This provides access these cards in the namespace

deck = Deck()
cards = Card.create_standard_52_cards()

deck.add_cards(cards)
# In the Python3 Interpreter:
# from main import deck, cards

# Launching point for the program
# It sits at the top level
# It is a sibling file with the 'poker' directory
from poker.card import Card

card1 = Card(rank = "2", suit = "Spades")
card2 = Card(rank = "Ace", suit = "Hearts")

# In the Python3 Interpreter:
# from main import card1, card2
# This provides access these cards in the namespace
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
hand3 = Hand()

player1 = Player(name="Ben", hand=hand1)
player2 = Player(name="Bobby", hand=hand2)
player3 = Player(name="Benita", hand=hand3)
players = [player1, player2, player3]

game = Game(deck=deck, players=players)
game.play()

for player in players:
    print(f"{player.name} receives a {player.hand}.")
    # Unpack the tuple into local variables
    index, hand_name, hand_cards = player.best_hand()
    hand_card_strings = [str(card) for card in hand_cards]
    hand_card_string = " and ".join(hand_card_strings)
    print(f"{player.name} has a {hand_name} with a {hand_card_string}.")

winning_player = max(players)
print(f"The winning player is {winning_player.name}.")

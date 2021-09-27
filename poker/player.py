class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __gt__(self, other):
        current_player_best_validator_index = self.best_hand()[0]  # 0
        other_player_best_validator_index = other.best_hand()[0]  # 7
        # The lower validator index is the more valuable hand of cards
        return current_player_best_validator_index < other_player_best_validator_index

    def best_hand(self):
        return self.hand.best_rank()

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        # Logic to build out later:
        # if self.wager_amount < self.amount_they_have_left:
        return False

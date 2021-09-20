class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def best_hand(self):
        return self.hand.best_rank()

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        # Logic to build out later:
        # if self.wager_amount < self.amount_they_have_left:
        return False

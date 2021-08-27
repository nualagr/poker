class Card():
    """
    Each card has required positional arguments
    rank and suit.
    """
    # Class Attributes
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
    RANKS = (
                "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "Jack", "Queen", "King", "Ace"
            )

    def __init__(self, rank, suit):
        # The Class Attribute will be available on every Class Instance so we can access it using 'self'
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")
        
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.SUITS}")
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card(rank = '{self.rank}', suit = '{self.suit}')"
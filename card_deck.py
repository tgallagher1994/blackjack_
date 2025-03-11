import random
#from card import Card  # Ensure card.py exists and is correct

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"
class Deck:
    def __init__(self):
        """Creates a full deck of 52 cards"""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(value, suit) for suit in suits for value in values]  # Creates 52 Card objects

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck (removes it)"""
        return self.cards.pop() if self.cards else None  # Avoids error if deck is empty
deck1 = Deck()
deck1.shuffle()
card1 = deck1.draw()
card2 = deck1.draw()
print(card1)
print(card2)
#card1 = Card("A", "Hearts")
#print(card1)  # A of Hearts
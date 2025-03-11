from tkinter import *
from tkinter import ttk
from card_deck import Deck

# Initialize root window
root = Tk()
root.title("Blackjack Game")
root.geometry("400x400")

# Label to display the drawn cards
output_label = ttk.Label(root, text="Click 'Start Game' to draw cards!", font=("Arial", 12))
output_label.pack(pady=10)

def startgame():
    """Starts the game, shuffles deck, draws two cards, and displays them."""
    deck1 = Deck()
    deck1.shuffle()
    card1 = deck1.draw()
    card2 = deck1.draw()
    
    # Display in GUI
    output_label.config(text=f"Card 1: {card1}\nCard 2: {card2}")

# Create and pack start button
start_button = ttk.Button(root, text="Start Game", command=startgame)
start_button.pack(pady=20)

# Run the application
root.mainloop()

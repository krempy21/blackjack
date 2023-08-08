Back-End Logic for the Blackjack game which shows a comprehensive overview and the core functionality of the game.

# Blackjack Game

Welcome to the Blackjack game! This is a simple text-based implementation of the classic casino card game Blackjack, also known as 21.

## How to Play

1. Run the `blackjack.py` script using Python. The game will prompt you to enter the number of games you want to play.

2. Follow the prompts to make decisions during each game:
   - After receiving two initial cards, choose whether to 'Hit' (draw another card) or 'Stand' (keep your current hand total).
   - If your hand total exceeds 21, you are busted and the dealer wins.
   - The dealer will automatically draw cards until their hand total is at least 17.

3. The game will display the result of each game and the winner (you or the dealer).

## Classes

The game is structured using classes, with separate classes for `Card`, `Deck`, `Hand`, and `Game`. Here's a brief overview of each class:

- `Card`: Represents a playing card with a suit and rank.
- `Deck`: Represents a deck of cards. The deck is initialized with standard cards and can be shuffled and dealt from.
- `Hand`: Represents a player's hand of cards. Calculates the hand's value, checks for blackjack, and displays the hand.
- `Game`: Manages the flow of the game, including gameplay loops, player decisions, and determining the winner.

## Game Logic

The game follows standard Blackjack rules:
- Aces can have a value of 1 or 11, depending on the hand's total.
- The goal is to have a hand total as close to 21 as possible without exceeding it.
- The dealer must draw cards until their hand total is at least 17.

## How to Run

1. Make sure you have Python installed on your system.

2. Open a terminal or command prompt and navigate to the directory containing the `blackjack.py` file.

3. Run the game using the command:
   ```
   python blackjack.py
   ```

## Have Fun!

Enjoy playing Blackjack and trying your luck against the dealer! Feel free to modify the code or add additional features to enhance the game.

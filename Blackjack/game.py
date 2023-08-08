from decks import Deck
from hands import Hand

class Game:

    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:

            try:
                games_to_play = int(
                    input("How many games do you need to play? "))
            except:
                print("you must enter a number")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_cards(deck.deal(1))
                dealer_hand.add_cards(deck.deal(1))

            print()
            print('*' * 30)
            print(f"Game {game_number} of {games_to_play}")
            print('*' * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "Hit", "s", "Stand"]:
                    choice = input(
                        "Please choose the valid options from '[H, Hit, S, Stand]' ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_cards(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_cards(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final results")
            print("Your Hand: ", player_hand_value)
            print("Dealer's Hand: ", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("Dang it! You are busted. Dealer Wins")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer is busted. You Win")
                return True
            elif player_hand.get_value() == 21 and dealer_hand.get_value() == 21:
                print("Both players have BlackJack. It's a tie")
                return True
            elif player_hand.get_value() == 21:
                print("You have BlackJack. You Win")
                return True
            elif dealer_hand.get_value() == 21:
                print("Dealer has BlackJack. Dealer Wins")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win")
                return True
            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie")
                return True
            else:
                print("Dealer Wins")
            return True
        return False


g = Game()
g.play()

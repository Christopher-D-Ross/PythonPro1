############### Our Blackjack House Rules #####################
import random

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []


def pull_card():
    return cards[random.randint(0, len(cards))]


def add_all_cards(array):
    count = 0
    for a in array:
        count += a
    return count


def clear_hands():
    player_cards.clear()
    computer_cards.clear()


def play_blackjack(response):
    if response == "y":
        clear_hands()
        player_cards.append(pull_card())
        player_cards.append(pull_card())
        computer_cards.append(pull_card())
        print(f"Your cards: {player_cards}, current score: {add_all_cards(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        another_card = ""
        computer_final_card_drawn = False
        while add_all_cards(player_cards) < 21 and another_card != "n":
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                player_cards.append(pull_card())
                print(f"Your cards: {player_cards}, current score: {add_all_cards(player_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
            elif another_card == "n":
                player_final = add_all_cards(player_cards)
                print(f"Your final hand: {player_cards}, final score: {player_final}")
                computer_cards.append(pull_card())
                computer_final_card_drawn = True
                computer_final = add_all_cards(computer_cards)
                print(f"Computer's final hand: {computer_cards}, final score: {computer_final}")
                if player_final < 21 and computer_final < 21:
                    if player_final > computer_final:
                        print("You Win")
                    elif player_final < computer_final:
                        print("You Lose")
                if player_final == computer_final:
                    print("Draw")
        if add_all_cards(player_cards) == 21:
            print("You Win")
        if add_all_cards(player_cards) > 21:
            print("You Lose")
        if not computer_final_card_drawn:
            player_final = add_all_cards(player_cards)
            print(f"Your final hand: {player_cards}, final score: {player_final}")
            computer_cards.append(pull_card())
            computer_final_card_drawn = True
            computer_final = add_all_cards(computer_cards)
            print(f"Computer's final hand: {computer_cards}, final score: {computer_final}")
            if player_final < 21 and computer_final < 21:
                if player_final > computer_final:
                    print("You Win")
                elif player_final < computer_final:
                    print("You Lose")
            if player_final == computer_final:
                print("Draw")
        play_blackjack(input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
    else:
        return


play_blackjack(input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))

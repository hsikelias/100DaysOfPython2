# https://appbrewery.github.io/python-day11-demo/
# assume a is 11 and 1 only if total sum count will reach above 21 and cards wont be removed every turn. 

import random
from art import logo

print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
choice = "y"

def shuffle_user_deck():
    """ 
    takes the cards list and then shuffles cards of the user and creating a new list. 
    The new list created will have 2 random cards. 
    """
    user_deck = random.sample(cards, 2)
    print(f"Your cards are: {user_deck}")
    return user_deck

def shuffle_computer_deck():
    """
    Shuffles cards of the computer and creating a new list
    """
    computer_deck = random.sample(cards, 2)
    print(f"Computer's first card is: {computer_deck[0]}")
    return computer_deck

def total_cards_sum(userCards):
    """
    Does the job of finding sums of the users cards. 
    Adjusts Ace (11) to 1 if sum goes above 21.
    """
    user_card_sum = sum(userCards)
    while 11 in userCards and user_card_sum > 21:
        ace_position = userCards.index(11)
        userCards[ace_position] = 1
        user_card_sum = sum(userCards)
    return user_card_sum

def add_user_cards(user_cards):
    """
    Adds new cards to the user deck if user chooses to hit.
    This function will require the user cards to actually add numbers to the list and it should return the sum  
    """
    should_continue = True
    while should_continue:
        choice = input("Enter 'y' to get another card or 'n' to end: ").lower()
        if choice == "y":
            new_card = random.choice(cards)
            user_cards.append(new_card)
            print(f"Your cards now: {user_cards}")
            total = total_cards_sum(user_cards)
            print(f"Your current score is: {total}")
            if total > 21:                       
                break
        else:
            should_continue = False
    return total_cards_sum(user_cards)

def dealer():
    """
    This function will do the job of managing bidders cards. 
    If user is done with their part then I take care of the bidder's logic, 
    I keep adding randomized cards to the bidder's cards till the count reaches equal to or above 17.
    """
    dealer_cards = shuffle_computer_deck()
    dealer_cards_sum = total_cards_sum(dealer_cards)
    while dealer_cards_sum < 17:
        dealer_cards.append(random.choice(cards))
        dealer_cards_sum = total_cards_sum(dealer_cards)
    print(f"The dealer's final hand is {dealer_cards} and the score is {dealer_cards_sum}")
    return dealer_cards, dealer_cards_sum

def game_logic(user_score, dealer_score):
    """
    Take cares of the game logic, determining if the user lose or not. 
    If user count and bidder count is equal, determine the draw logic. 
    If the user total sum is > 21 then "player lost" but if player stands then compare the values of user sum and dealer's sum and determine the winner.
    """
    print(f"\nFinal Results:\nYour score: {user_score}\nDealer's score: {dealer_score}")
    if user_score > 21:
        print("You went over 21. You lose")
    elif dealer_score > 21:
        print("Dealer went over 21. You win")
    elif user_score > dealer_score:
        print("You win")
    elif dealer_score > user_score:
        print("You lose")
    else:
        print("It's a draw")

def run_game():
    """
    Asks user if they want to play the game, call this function at the beginning of the game 
    and after the user completes the game. 
    """
    global choice
    while choice == "y":
        print("\n"*5)
        userPlay = input("Do you want to play a game of black jack? Type 'y' or 'n': ").lower()
        if userPlay == "y":
            print("Alright lesgo! \n3\n2\n1\n....\n")
            user_cards = shuffle_user_deck()
            final_user_score = add_user_cards(user_cards)
            dealer_hand, final_dealer_score = dealer()
            game_logic(final_user_score, final_dealer_score)
        elif userPlay == "":
            run_game()
        else:
            print("Thanks for visiting us!")
            choice = "n"
            exit()

run_game()

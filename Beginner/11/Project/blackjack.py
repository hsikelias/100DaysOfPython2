# https://appbrewery.github.io/python-day11-demo/


import random
from art import logo

print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def cardsDealer():

  """
  I do the job of randomizing cards and assigning them to the users cards and computer cards. I also update the total count of computer and user cards. 
  """

def gameLogic():

  """
  I take care of the game logic, that involves tracking the total sum count of user and then determining if they lose or not. If user stands then I take care of the bidders logic, I keep adding randomized cards to the bidders cards till the count reach equal to or above 17. If user count and bidder count is equal, i determine the draw logic. 
  """

def game():

  """
  Asks user if they want to play the game, call this function at the beginning of the game and after the user completes the game. 
  """

  userPlay = input("Do you want to play a game of black jack? Type 'y' or 'n': ").lower()
  if userPlay == "y":
    print("Alright lesgo!")
    # cardsDealer()
  elif userPlay == "":
    game()
  else:
    print("Thanks for visiting us!")
    exit()

# next steps for me is to randomize the cards from [cards] and create a list of user cards, total score calc, 

game()

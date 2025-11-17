'''
You have bunch of cards, user chooses wether to hit or stand, u repeat asking if they want to hit or stand while the card amount is below or = to 21.
If the card amount crosses 21, bidder wins! each caard has its own value. 
from 2 - 10, count as their face values so 6 is 6, 9 is 9, but jack, queen, and king each count as 10. Ace can be either counted as 1 or 11, u choose which value
ace to represent. 
You can't see dealers card, dealer must take another card till they pass 17. If yuu and dealer have same amount of card value then its a draw. 

Our game: 

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
// counted as 11 only if the overall user card value goes over 21

The card is not removed

things in the final project:
current score tracker
list of my cards
orginal cards
showing computers card
computer wont stop until u bust
'''
# import necessary libraries

import random
from art import logo

def clearScreen():
    print("\n"*100)
    print(logo)
    
print("hello world")
clearScreen()
import random

symbols = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
'''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

def computer_choice():
    compchoice = random.choice(symbols)
    computer_choice

print("Welcome to this amazing rock, paper, scissors game!")
user_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissors"))

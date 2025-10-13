import random

rock= [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
]

paper = [
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,   ]


scissors = [    
'''    _______
---'      ____)____
        ______)
    __________)
    (____)
---.__(___)
'''
]

game_images = [rock, paper, scissors]

print("Welcome to this amazing rock, paper, scissors game!")
user_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissors"))
print([game_images[user_choice]])


computer_choice = random.randint(0, 2)
print(f"Computer chose:{computer_choice}")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

elif user_choice == 0 and user_choice == 2:
    print("Y Wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")

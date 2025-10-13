print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

left_right_direction = input("    Type \"left\" or \"right\"    ").lower()

if left_right_direction == "left":
    swim_wait = input("You've reached to a small river, it is said that there are pirannhas at this moment. Are you brave enough to swim through them? \n Or will you be smart enough to wait till the sun rises? swim/wait?").lower()
    if swim_wait == "wait":
        door = input("You've come past the river and now you've approached 3 doors in red/blue/yellow. Which one will you choose?").lower()
        if door == "red":
            print("You enetered the pathway to the depths of hell and have been burnt to crisp, game over!")
        elif door == "blue":
            print("You've entered the deepest depths of ocean and drowned to death, game over!")
        elif door == "yellow":
            print("You reached honey land filled with golden treasure, you won the game!")
        else:
            print("Invalid input, only red/blue/yellow is allowed")
    else:
        print("Game Over, you died trying to swim through a river filled with pirranhas")

elif left_right_direction == "right":
    print("Game over!")
else:
    print("Invalid input only left/right is allowed!")
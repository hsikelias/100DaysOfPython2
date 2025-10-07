import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
symbol = [
'''
        ------
	|   | 
	|    
	|  
	|    
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  
	|    
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|   |
	|   
	|   
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|
	|    
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|\\
	|    
	|   
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|\\
	|   | 
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|\\
	|   | 
	|  /
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|\\
	|   | 
	|  / \\
	| 
	--------- 
''',
'''
        ------
	|   | 
	|    
	|  
	|            O
	|           /|\\
	|            |
	---------   / \\
'''
]

words = [
    "python",
    "elephant",
    "bicycle",
    "astronaut",
    "computer",
    "pizza",
    "kangaroo",
    "umbrella",
    "mountain",
    "library",
    "diamond",
    "volcano",
    "sandwich",
    "giraffe",
    "rainbow",
    "suitcase",
    "dolphin",
    "pancake",
    "wizard",
    "galaxy"
]


lives = 8
chosen_word = random.choice(words)
blank_word = ["_" for _ in chosen_word]
gussed_letters = []


print(logo)
print("Welcome to Hangman! Below is your word, start guessing letters!\n")

while lives > 0:
    print(" ".join(blank_word))
    print(symbol[8 - lives]) 

    guess = input("\nEnter a letter: ").lower()

    if guess in gussed_letters:
        print("You already guessed that letter.")
        continue
    gussed_letters.append(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                blank_word[i] = guess
        print("Nice guess!")
    else:
        lives -= 1
        print("Wrong guess!")
    
    if "_" not in blank_word:
        print(f"\nYou won! The word was '{chosen_word}' indeed.")
        break

else:
    print(symbol[-1])
    print(f"\n You lost! The word was '{chosen_word}'.")

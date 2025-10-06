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


print(logo)

print("Welcome to Hangman! Below is your word, start guessing letters!!\n")

print(blank_word)
print("\n")
print(chosen_word)    # REMOVE THIS LATER, RN ITS JUST HERE FOR DEBUGGING

print(symbol[lives])
guess = input("Enter your letter guess:").lower()

while lives > 0:
	for letter in chosen_word:
		if letter == guess: 
            print('Nice guess!')
        else:
            lives -= 1
            print(symbol[lives])

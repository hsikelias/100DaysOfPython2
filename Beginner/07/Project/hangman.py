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


lives = 7
random_word = random.choice(words)
blank_word = ["_" for _ in random_word]


print(logo)

print("Welcome to Hangman! Below is your word, start guessing letters!!")

print(blank_word)
print(random_word)

# assuming the word is wizard

while lives > 0:   # checks if lives are left and if there are still blanks

  guess = input("Enter your letter guess:").lower()  # takes input from the letter, #assume user enters "a", a is in 
	# now i need to check if the letter is in the word
  if guess in random_word: 
    # guess is a and a is infact in wizard and its at 4
    print
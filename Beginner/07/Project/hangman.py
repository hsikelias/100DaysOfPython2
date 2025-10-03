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


lives = 9
random_word = random.choice(words)
blank_word = ["_" for _ in random_word]


print(logo)

print("Welcome to Hangman! Below is your word, start guessing letters!!")
print(blank_word)

# assuming the word is wizard

while lives > 0 and "_" in blank_word:   # checks if lives are left and if there are still blanks
    guess = input("Enter your letter guess:").lower()  # takes input from the letter
    
	# now i need to check if the letter is in the word
    if guess in random_word: # checks if the guessed letter in the picked word
        # now i need to identify the correc index of the letter
        for position in range(len(random_word)): # finding the length of the word
            letter = random_word[position] # since we have the position now i can find the letter 
	    if letter == guess:
			blank_word[position] = letter # now i can replae the blank with the letter

            
	    

	


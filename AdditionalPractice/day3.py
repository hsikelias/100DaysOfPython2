import random

# Word list
word_list = ["aardvark", "baboon", "camel"]

lives = 6

word = random.choice(word_list)

blank_word = ["_"] *len(word)
print(f"Your word hint is {blank_word}, start guessing!!")


while lives != 0:
    guess = input("Guess a letter from this word: ").lower()
    found = False

    for i in range(len(word)):
        if word[i] == guess:
            blank_word[i] = guess
            found = True 

    if "_" not in blank_word:
        print(f"You win!! word was {word}")
        break            
    if found:
        print(f"Correct! updated: {blank_word}")
    else:
        lives -= 1
        print(f"Wrong,You have {lives} lives.. try another guess")

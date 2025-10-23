import random
import hangman_words
# another way is to add a from statement to words so u can make the program code little simpler
from art import symbol

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(hangman_words.word_list)
lives = 6
display = ""

print("Welcome to hangman!")
print("Below is your word, start guessing, one letter at a time!")

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
  placeholder += "_" 
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
  guess = input("Guess a letter: ").lower()

  if guess in correct_letters:
    print("You've already guessed this letter, try another one!")

  display = ""  

  for letter in chosen_word:
    if letter == guess: 
      display += letter
      correct_letters.append(letter)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"

  print(display)
  if guess not in chosen_word:
    lives -= 1
    print(f"You have these many lives left: {lives}")
    if lives == 0:
      game_over = True
      print("You lost!")


  if "_" not in display:
    game_over = True 
    print("You win!")

  print(symbol[lives])

  # so now we gotta use whiles to loop thru a logic, in the while loop the program should repeat the process of prompting user to enter the word till either there are no "_" and lives is above 0


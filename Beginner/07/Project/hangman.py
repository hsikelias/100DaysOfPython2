import random
art = []
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
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

  display = ""  

  for letter in chosen_word:
    if letter == guess: 
      display += letter
      correct_letters.append(letter)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"
      lives -= 1

  print(display)

  if "_" not in display:
    game_over = True 
    print("You win!")



  # so now we gotta use whiles to loop thru a logic, in the while loop the program should repeat the process of prompting user to enter the word till either there are no "_" and lives is above 0


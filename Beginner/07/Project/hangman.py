import random

word_list = ["aardvark", "baboon", "camel"]
pickedWord = random.choice(word_list)
lives = 7
print(pickedWord)

hiddenWord = "_"*len(pickedWord) # lesgo we got the words replaced to _
hiddenList = list(hiddenWord)  # converting the hidden word, whichs in a string to a list. we do this cus lists makes it easier to update blanks and more control basically.

print("Welcome to hangman!")
print("Below is your hidden word, start guessing, one letter at a time!")
print(hiddenWord) 
print(hiddenList)  

while lives >0 and "_"  in hiddenList:
  guess = input("Guess a letter: ")
  if guess in pickedWord:
    enumerate(pickedWord)
    print("Your guessed letter is correct!")
  elif guess == hiddenList:
    print("Entered guess is already guessed, try a new letter!")
  elif guess != hiddenList:
    print("Wrong guess")
  else:
    print("You entered "+ guess+",you might've entered a number, please enter only one letter!")

# need to convert the hidden word variable to list. 
# so with this i get the position of the letter but in the case of the multiple characters it doesnt give out every single character. like in baboon.. if i say b it doesnt give out 0,2.. only 0.
# so this method is really awful because i want the user to get all the existing letters.


    print(hiddenList)
  


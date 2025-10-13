# Randomisaion and Python Lists

import random
"""
rando = random.random()
print(rando)"""


"""
random_float = random.uniform(5,6)
print(random_float) 

"""
"""
            #0        #1       #2        #3
fruits = ["apple", "corn", "orange", "tomato"]
            #-4      #-3      #-2         #-1   
print(fruits[-4]) """

"""
Lottery Simulator

Generate 6 random numbers between 1 and 49 (no repeats).

Store them in a list and print them sorted.

"""
"""
# convering a list into string

ran_num = random.choices(range(1,50),6)
result = ", ".join(str(item) for item in ran_num)
print(result)

"""

# for loop
"""
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pear")
    print(fruit)

"""
"""
while True:
    for item in fruits:
        print(fruits) 
"""

#loops with range
"""
for number in range(5,11):
    print(number)
"""

'''
Easy Version
Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

4 letters 2 symbols and 3 numbers then the password might look like this:

fgdx$*924

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

Hint 1 
Hard Version
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different.
'''
"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordlist = []

rand_letters = random.choices(letters,k = nr_letters)
rand_numbers = random.choices(numbers,k = nr_numbers)
rand_symbols = random.choices(symbols,k = nr_symbols)

print(rand_letters)
print(rand_numbers)
print(rand_symbols)

passwordlist = rand_letters + rand_numbers + rand_symbols
random.shuffle(passwordlist)
final_password = "".join(str(item) for item in passwordlist)
print(final_password)
"""

"""
def is_even():
    return num%2 == 0

repeat = True
while repeat:
    num= int(input("Enter a number:"))
    print (is_even(num))
    repeat = input("continue? y/n: ")
    if repeat.lower() != 'y':
        repeat= False
"""
"""
def grade_score(avg_score):
    if avg_score >= 90:
        return("A")
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 70:
        return "C"
    elif avg_score >= 60:
        return "D"
    else:
        return "F"

exam1 = int(input("Enter exam1 grade: "))
exam2 = int(input("Enter exam2 grade: "))
exam3 = int(input("Enter exam3 grade: "))
avg_score = (exam1 + exam2 + exam3)/3

print(f"Your average score is {round(avg_score)} and grade is {(grade_score(avg_score))}")

"""
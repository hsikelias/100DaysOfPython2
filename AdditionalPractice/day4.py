#functions
"""
def greet():
    print("Hi")
    print("Hello")
    print("What up")


greet()"""

"""
def greet_with_name(name):
    print(f"Hi {name}")
    print(f"Hello {name}")
    print(f"What up {name}")
"""


# name here is the parameter, and the input you get from name is the argument
# parameter is the name of the data, argument is the value.
"""
def life_in_weeks(age):
    maxage =90
    leftage = maxage-age
    oneage = 52 #weeks
    x = 52*leftage
    print(f"You have {x} weeks left")

age = int(input("What is your age?: "))
life_in_weeks(age)
"""

#functions with more than 1 input
def greet_with(name,location):
    print(f"Helo {name}")
    print(f"What is it like in {location}?")

# my_function(Lekish, Bangalore)
# my_function(Bangalore, Lekish)
# changing this will affect the order it prints too, positional arguments
# to make it work regardless of the order: 
    """
    def my_function(a,b,c):
    # Do this with a
    # Then do this with b
    # Finally do this with c

    my_function(a=1,b=2,c=3)
name = input("What is your name?: ")
location = input("Where are you from?: ")
greet_with(name,location)
"""
"""
def calculate_love_score(name1, name2):
    True_count = 0
    Love_count = 0
    fullname = (name1+name2).lower()
    True_count = fullname.count('t') + fullname.count('r')+fullname.count('u')+fullname.count('e')
    Love_count = fullname.count('l') + fullname.count('o')+

    true_score_str = str(True_count)
    love_score_str = str(Love_count)
    final_score_str = true_score_str + love_score_str
    print(f"{name1} and {name2}, Your love score is {final_score_str}")


calculate_love_score(name1 = "Kanye West",name2 = "Kim Kardashian")
"""

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


alphabets = ["a","b","c","d","e","f","g","h", "i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = "" #h
    if encode_or_decode == "decode":
                shift_amount *= -1

    for char in original_text:

        if char not in alphabets:
            output_text += char
        else:
            

            shifted_position = alphabets.index(char) + shift_amount #10 -> 8
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_contniue = True

while should_contniue: 

    direct = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = str(input("Enter the message:\n").lower())
    shift = int(input("Type the shift number:\n"))

    ceaser(original_text=text, encode_or_decode=direct,shift_amount=shift)

    restart=input("Type 'yes'if you want to go again. Otherwise, type 'no'\n").lower()

    if restart == "no":
        should_contniue = False
        print("Good bye king!")
# _ _ _ _ _ _

# 1 3 0 2 0 8

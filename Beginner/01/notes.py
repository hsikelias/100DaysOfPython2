
print("What's up")

# this is a print function,  what u want to print is between the double quotes.
# the key word here is print

# adding things inside the double quotes tells the computer that whatever is inside it
# is not a code, its called STRING. Double quotes show the beginning and end of the string.

# when you face an error, just copy paste it to google and use sources like stackoverflow to get answers. 
# Every porgrammer makes a mistake, you just have to be good at figuring out the problem.

# not just double quotes we can also use single quotes

print('"Hello"')
print("Hey's")

print("Hello World")
print("Hello World")
print("Hello World")

# This takes too much space just for wanting to print in a new line, we can use \n to create a new line. 

#\n This moves the next string to new line
print("Yeezy season approachin \nfk what yall been hearin")

# concataate strings
print("Gurt:"+" yo")
print("Hello"+" Whats up")

# space is very important in python, you will face an Indentation error in such cases.
# sometimes there might not be an issue in indentation but in complex programs involving if/else/loops its important
# to understand where to place your code. 


# you get a syntax error if you make any mistakes like forgeting to close a string statement  with "


# INPUT: we use this when we want the user to enter some data. Instead of print, which we enter the data our self.. we use input to
# ask the user to enter something
# - Inputs are string at default

input("What is your name: ")

# currently the input function does ask the user for data, but we're not using it anywhere yet

print("Hello "+ input("What is your name: ")+ "!")
# another use of string concatination. Now we can greet the user


# VARIABLES: before we did ask the user for a name, but it just ends with asking the name..
# we use variables to actually refer to that data later.

username = input("Whats your name ")
len_username = len(username) #so now we can use name data for whatver and whenever we want

print(username)
print(len_username)

# Variable Naming

# be clear with how you name variables.
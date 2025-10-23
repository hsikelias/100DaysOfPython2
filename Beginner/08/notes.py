# Functions

# def my_function():
# if u remember this is how u define the functions, under the function u ask for whatveer u want it do 
# and then u call the function by 
# my_function()
'''
def greet():
    print("Welcome")
    print("Welcome")
    print("Welcome")
greet()
'''
# FUNCTIONS WITH INPUTS

# what if we want to do something with the things inside the function like if my function currently says hello someone and
# maybe for next time its someone2 so basically functions with input, in that case look closely at the () in functions.. that is to add a variable inside that ()

def greet2(name,age,location): # multiple inputs 
    print(f"Hello {name}")
    print(f"Youre {age}")
    print(f"You live in {location}")
          
greet2("Bob","8","Brooklyn")   # the data is over here, "Bob".. it takes and sends it to the function to be called with the variable mentioned
# the order obviously matters.. this method is called Positional argument

# if you do NOT want to worry about the order in that case you can include the variable too.. below method is called key argument.
greet2(age=10,name="roma",location="brooklyn")

name = "Bob"
# paramater is the name of the data
# argument is the bob, its data
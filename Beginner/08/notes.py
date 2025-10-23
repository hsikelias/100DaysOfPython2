# Functions with inputs

def greet():
    print("Hey")
    print("How do you do")
greet()

# the above example is the common way to use functions. You use greet() to call the function. As per the example, if you had to greet the user with their name you could 
# hard code it or be smart and use functions a little better

def greetWithName(name): #parameter is the name of the data and the argument is its value.. like name is the parameter and whatever its value, is the argument
    print("Hello " + name)
    print("How do you do?")

greetWithName("Arun")  # inside of this, you add the variable data because whatevers here will be sent to the function to do its job

# POSITIONAL VS KEYWORD arguments

# what if you want to add multiple parameteres.. you can do that the way u add single parameters but you just need to seperate them with a ,

def greetComplex(name, age, location):
    print(f"Hello {name}")
    print(f"You are {age} years old")
    print(f"and you are from {location}.")

# the order obv matters but it only does in positional argument..
greetComplex("Laurie",18,"New York City")

# if you dont want to worry abt order u can use keyword arguments to specify the parameters value when calling the function itself
greetComplex(name="Laurie",age=18,location="New York City")


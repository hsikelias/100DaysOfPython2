"""

def add(n1, n2):
    return n1 + n2

# function for each and every operation, storing function as a value of variable

my_fav_operation = add  #cant add ( ) because it will trigger a function, now obv we still need to find a way to add inputs. 

# as we gave the add values to fav operation, we can add the inputs to this new variable
print(my_fav_operation(2,3))

"""


"""
## FUNCTIONS INSIDE A DICTIONARY 

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

dic1 = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}
# Use dic1 operations to perform the caluclation, multi 4 * 8
print(dic1["*"](2,3))

"""


def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": division,
}


def caluclator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
# for operations, angela used dictionaries instead damn
        num2 = float(input("What is the second number?:"))
# float instead of int
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue caluclation with {answer}, or type 'n' to start a new caluclation.")
    
        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            caluclator()

caluclator()

# has a recurrsion feature, basically all the program codein a function and inside the function u add another function to repeat the whole process... so creative. 
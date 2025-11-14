# This is the same code but Im rebuilding the program from scratch with a better code solution
from art import logo

def add (n1,n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mul (n1, n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

# Bunch of defs for each operation.

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator(): 
    shouldContinue = True
    print(logo)
    num1 = int(input("Enter your first number: "))
    while shouldContinue: 
        for opr_symbol in operations:
            print(opr_symbol) 
            
        opr = input("Enter the operation you want to do: ")
        num2 = int(input("Enter your second number: "))

        answer = operations[opr](num1,num2)
        print(answer)
        print(f"{num1} {opr} {num2} = {answer}")

        choice = input("Type 'y' if you want to continue the calculation with the current answer "
        "or type 'n' if you want to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            shouldContinue = False
            print("\n*100")
            calculator()
calculator()
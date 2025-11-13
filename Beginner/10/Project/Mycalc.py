from art import logo
print(logo)

def mainCalc (fNum, sNum,opr,choice):  
    """
    This function does the job of completing the selected operation and then have a loop that reuses the first num value to repeat the first number.  
    The function has bunch of if statements to do the operation and then we will do a while loop 
    
    """ 
    while choice == "y":
        if opr == "+":
            answer = fNum + sNum
        elif opr == "-":
            answer = fNum - sNum
        elif opr == "*":
            answer = fNum * sNum
        elif opr == "/":
            answer = fNum / sNum
        else:
            print(f"Enter only provided operations, you responded {opr}")
        print(f"{fNum} {opr} {sNum} = {answer}\n")

        print("Do you want to continue the game?")
        continueOrNot = input("Type 'y' if you want to continue and 'n' if you want to exit. ").lower()

        if continueOrNot == "y":
            print("+ \n- \n* \n/ \n")
            opr =input("Now, please enter the operation you want to do: ")
            sNum = int(input("Please enter your second number: "))
            fNum = answer
            choice = "y"
        else:
            choice = "n"
            exit()
    
    # PROGRAM WORKS PROPERLY, well kind of.. the problem is that when user enters y it doesnt ask the user for a new operation and second number. 
choice = "y"

firstNum = int(input("Please enter your first number: "))
print("+ \n- \n* \n/ \n")
operation =input("Now, please enter the operation you want to do: ")
secondNum = int(input("Please enter your second number: "))

mainCalc(firstNum,secondNum,operation,choice)



# HOW DOES MY PROGRAM WORK: 

#
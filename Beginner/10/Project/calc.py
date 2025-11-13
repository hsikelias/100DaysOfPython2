from art import logo
print(logo)


def mainCalc (fNum, sNum,opr):  
    """
    This function does the job of completing the selected operation and then have a loop that reuses the first num value to repeat the first number.  
    """ 
    
    if opr == "+":
        answer = fNum + sNum
    elif opr == "-":
        answer = fNum - sNum
    elif opr == "*":
        answer = fNum * sNum
    elif opr == "/":
        answer = fNum / sNum
    else:
        print("Print given operations")
    # completes first iternation
    print(f"Your answer is {answer}")

    print("Do you want to continue the game?\n")
    continueOrNot = input("Type 'y' if you want to continue and 'n' if you want to exit. ")
    if continueOrNot == "y":
        print("Alright lets do this again..")
    else:
        exit()
    return answer
    

def secondMainCalc (fNum, sNum,opr,choice):
    print("test")



firstNum = int(input("Please enter your first number: "))
print("+ \n- \n* \n/ \n")
operation =input("Now, please enter the operation you want to do: ")
secondNum = int(input("Please enter your second number: "))

mainCalc(firstNum,secondNum,operation)
# atp user will get the answer and its time to ask if they want to continue

print("Do you want to continue the game?\n")
continueOrNot = input("Type 'y' if you want to continue and 'n' if you want to exit. ")
if continueOrNot == "y":
    choice = continueOrNot

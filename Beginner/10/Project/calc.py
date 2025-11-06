from art import logo
choice = "y"
print(logo)

# program starts with asking the user first number and then displays bunch of operations( +, -, *, /). Then it asks for user to enter the operation.
# Then the program asks user for another number. After entering the number the program pritns the caluclation and answer. 
# Then a new prompt which asks y to save the previous answer for next caluclation or n for starting a new caluclation. 

def mainCalc (fNum, opr, sNum):
  if opr == "+":
    answer = fNum + sNum
  elif opr == "-":
    answer = fNum - sNum
  elif opr == "*":
    answer = fNum * sNum
  elif opr == "/":
    answer = fNum / sNum
  else:
    print("Make sure you entered valid operations!")
  print(answer)

while choice == "y":
  firstNum = int(input("Enter your first number: "))
  operation = input(f"Choose one: \n + \n - \n * \n / \n")
  secondNum = int(input("Now enter your second number: "))

  mainCalc(firstNum,operation,secondNum)

  option = input("Do you want to continue? y for yes and n for no: ")
  if option != "y":
    choice = "n"
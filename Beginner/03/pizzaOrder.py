print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
cost = 0 

if size == "S":
    print("Small size pizza costs $15")
    cost +=15
elif size == "M":
    print("Medium size pizza costs $20")
    cost += 20
elif size == "L":
    print("Large size pizza costs $25")
    cost +=25
else:
    print("Wrong input yo. make sure its either S/M/L")

if pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost +=3

if extra_cheese == "Y":
    cost +=1

print(f"Your total bill is ${cost}")
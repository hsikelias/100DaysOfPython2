'''
print("Welcome to the rollercoaster")
height = int(input("Enter your height"))
if height>= 120:
    print("You can ride the rollercoaster")
    age = int(input("Now, What's your age?"))

    if age <= 12: # if the age is less than 12
        print("Pay $5")
    elif age <= 18: # this happens when age is NOT less than 12 but this also checks if age is under 18
        print("pay $7")
    else:
        print("Pay $12")
else:
    print("womp womp u cant ride the rollercoaster")

'''
    # a tip for if/elif logic.. when u type a condition think of what happens if its NOT true
    # my previous method was long and it involved AND operator for no resaon.. this new version
    # is much simplified and its better, i missed the "what if its not" logic


print("Welcome to the rollercoaster")
height = int(input("Enter your height"))

bill = 0
if height>= 120:
    print("You can ride the rollercoaster")
    age = int(input("Now, What's your age?"))

    if age <= 12: # if the age is less than 12
        bill = 5
        print("Child tickets are $5")
    elif age <= 18: # this happens when age is NOT less than 12 but this also checks if age is under 18
        bill = 7
        print("Youth tickets are $7")
        
    elif age >= 45 and age <=55:
        print("free ride!")
    else:
        bill = 12
        print("Adult tickets are $12")

    pic = input("Do you want a pic? y for yes and n for no")
    if pic == "y":
       bill +=3
    
    print(f"Your final bill is {bill}")
else:
    print("you cant ride")

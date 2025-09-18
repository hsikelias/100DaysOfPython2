print("Welcome to the Tip Caluclator")
bill = int(input("Enter the total bill amount: $"))
tip = int(input("How much tip would you like to give?: $"))
split = int(input("How many people are splitting the bill?: "))

totalBill = bill + tip
onePersonBill = totalBill/split

print(f"Each person should pay ${onePersonBill}")
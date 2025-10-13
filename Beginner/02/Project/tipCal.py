print("Welcome to the Tip Caluclator")
bill = float(input("Enter the total bill amount: $"))
tip = int(input("How much tip would you like to give?: $"))
split = int(input("How many people are splitting the bill?: "))

tip_percent = tip/100
total_tip = bill*tip_percent
total_bill = total_tip + bill
onePersonBill = total_bill/split

print(f"Each person should pay ${round(onePersonBill)}")
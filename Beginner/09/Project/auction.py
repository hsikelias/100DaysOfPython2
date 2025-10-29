from art import logo


print(logo)
print("Welcome to the Auction! Start Bidding!")
other_bidders = "yes"
bids = { }

# TODO-1: Ask the user for input
while other_bidders == "yes":
  name = input("Enter your name: ")
  price = float(input("Enter your bid amount: $"))
# TODO-2: Save data into dictionary {name: price}
  bids[name] = price
  print("\n"*100)
  print(bids)
# TODO-3: Whether if new bids need to be added
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()



# TODO-4: Compare bids in dictionary

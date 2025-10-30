from art import logo


print(logo)
print("Welcome to the Auction! Start Bidding!")
other_bidders = "yes"
bids = { }

while other_bidders == "yes":
  name = input("Enter your name: ")
  price = float(input("Enter your bid amount: $"))

  bids[name] = price
  print("\n"*100)

  other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

key_value = max(bids.items(),key=lambda item: item[1])
winner_name = key_value[0]
winner_amount = key_value[1]

print(f"The highest bid was $ {winner_amount} bidded by {winner_name}. Congratulations!!")

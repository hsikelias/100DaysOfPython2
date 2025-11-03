from art import logo

def winner():
  key_value = max(bids.items(),key=lambda item: item[1])  # the key_value is trying to find the highest amount, max is used checking bids.items() our key is 
  winner_name = key_value[0]
  winner_amount = key_value[1]
  print(f"The highest bid was $ {winner_amount} bidded by {winner_name}. Congratulations!!")

print(logo)
print("Welcome to the Auction! Start Bidding!")
other_bidders = "yes"
bids = { }  #stores all the bidders and bid amount lets say {"Trio":5,"Mary":6}

while other_bidders == "yes":   # while theres more bidders
  name = input("Enter your name: ")
  price = float(input("Enter your bid amount: $"))

  bids[name] = price
  print("\n"*100)

  other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
winner()


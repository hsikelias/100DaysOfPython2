name = input("What is your name?: ")
price = input("What is your bid? $")


bids = {}

bids[name] = price
should_continue = input("Are there any other bidders? Type 'y' for yes and 'n' for no. \n")

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = input("What is your bid? $")


from art import logo
bids = {}
print(logo)

def find_highest_bidder(bidding_dictionary):    # inside this we can add a parameter like a dictionary in our case.
    winner=" "
    highest_bid = 0;
    for bidder in bidding_dictionary:           # so this will find the bidder name, not the amount
        bid_amount = bidding_dictionary[bidder] # to access the amount bidded, we do this. We need to figure out the largest number.
        if bid_amount >highest_bid:            
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")
# without max one way to check the largest number is to compare the bid_amount to the next users bid amount contionously. OR we can give the bid amount
# value to a variable and then everytime we loop js check if bid amount is great/less than the highest bid till we compelte the dictionary. 

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'y' for yes and 'n' for no. \n").lower()

    if should_continue == "n":
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue == "y":
        print("\n"*20)


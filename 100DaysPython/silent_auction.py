import os
clear = lambda: os.system('cls')
#HINT: You can call clear() to clear the output in the console.
auction_is_open = True
list_of_bids= []

clear()
print("Welcome to the silent auction.")

while auction_is_open:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    list_of_bids.append({"name": name, "bid": bid})
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bids.lower() == "no":
        auction_is_open = False
        clear()
    else:
        clear()

max_bid = 0
max_bidder = ""

for bid in list_of_bids:
    if(int(bid["bid"]) > max_bid):
        max_bid = int(bid["bid"])
        max_bidder = bid["name"]

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
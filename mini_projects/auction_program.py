import os
from auction_program_art import logo

print(logo)
bids = {}


def silent_auction(name, bid):
    bids[name] = bid


yes_or_no = ""

while yes_or_no != "no":
    bidder_name = input("What is your name?: \n")
    bidders_bid = int(input("What is your bid?: \n"))
    silent_auction(bidder_name, bidders_bid)
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if yes_or_no == "yes":
        os.system("clear")


highest_bidder = ""
highest_bid = 0
for key in bids:
    if bids[key] > highest_bid:
        highest_bidder = key
        highest_bid = bids[key]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
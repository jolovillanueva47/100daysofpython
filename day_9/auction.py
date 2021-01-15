from replit import clear
from art import logo
print(logo)
bidders={}
there_are_still_bidders=True
def  check_highest_bidder(bidders_list):
    highest_bid=0
    highest_bidder=""
    for bidder in bidders_list:
        if bidders_list[bidder] > highest_bid:
            highest_bid=bidders_list[bidder]
            highest_bidder=bidder
    print("--------------AUCTION RESULT--------------")
    print(f"\nThe winner is {highest_bidder} with a bid of ${highest_bid}.")
while there_are_still_bidders: 
    print("Welcome to the secret auction program.")
    bidder_name=input("What is your name?: ")
    bidder_bid=int(input("What is your bid: $"))
    bidders[bidder_name]=bidder_bid
    bidders_left=input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if bidders_left=="no":
        clear()
        print(logo)
        check_highest_bidder(bidders)
        there_are_still_bidders=False
    else:
        clear()
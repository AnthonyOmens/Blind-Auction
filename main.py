# This is a blind auction program. Enter you name and bid ammount. Selet Y if there more people who want to bid and pass the laptop

from replit import clear
from art import logo

bid_data_base = {}

more_ppl = True

while more_ppl == True:
  print(logo)
  name = input("What is your name?\n")
  bid = int(input("What is your bid? $"))
  
  bid_data_base[name] = bid
  #sets name: bid in dict
  
  #print(bid_data_base)
  #uncomment this ^ if you want to see dict
  more_ppl_input = input("Are there more people?\nY or N").lower()

  if more_ppl_input == "y":
    more_ppl = True
    clear()
  else:
    more_ppl = False

highest_bid = max(bid_data_base, key=bid_data_base.get)
#max() makes this so much easier

print(f"The person with the highest bid is {highest_bid} with ${bid_data_base[highest_bid]}")

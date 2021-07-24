import random

prompt = True

while prompt == True:
    random_number = random.randint(1, 6)
    print(random_number)

    again = input("Do you want to roll the dice again? (y/n)")
        
    if again == "n" or again == "N":
        prompt = False

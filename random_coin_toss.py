import random

again = "y"

for i in range(10):
    heads_tails = random.randint(1, 2)

    if heads_tails == 1:
        print("Heads")
    else:
        print("Tails")

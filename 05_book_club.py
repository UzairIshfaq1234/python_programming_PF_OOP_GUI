number_of_books = int(input("Enter the number of books purchased: "))
points = 0

if number_of_books == 1:
    points = points + 5
elif number_of_books == 2:
    points = points + 15
elif number_of_books == 3:
    points = points + 30
elif number_of_books >= 4:
    points = points + 60

print(f"You have bought {number_of_books} books")
print("---------")
print(f"You have earned {points} points!")

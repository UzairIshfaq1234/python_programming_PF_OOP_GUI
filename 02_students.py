total = 100

def if_exceeds(marks):

    if marks < 0:
        print("Please enter a value greater than 0")
        exit()

    if marks > total:
        print("Please enter a value less than 100")
        exit()

test_1 = float(input("Enter your marks for the first test: "))
if_exceeds(test_1)

test_2 = float(input("Enter your marks for the second test: "))
if_exceeds(test_2)

test_3 = float(input("Enter your marks for the third test: "))
if_exceeds(test_3)

average = (test_1 + test_2 + test_3) / 3

print(average)

if average > 95:
    print("Congratulations for scoring a good score!")

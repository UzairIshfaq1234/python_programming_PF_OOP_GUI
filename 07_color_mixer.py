colour1 = input("Enter the first primary colour: ")
colour2 = input("Enter the second primary colour: ")

mixed_colour = ""

if (colour1 == "red" or colour1 == "blue" or colour1 == "yellow") and (colour2 == "red" or colour2 == "blue" or colour2 == "yellow"):

    if (colour1 == "red" and colour2 == "blue") or (colour2 == "red" and colour1 == "blue"):
        mixed_colour = "purple"
    elif (colour1 == "red" and colour2 == "yellow") or (colour2 == "red" and colour1 == "yellow"):
        mixed_colour = "orange"
    elif (colour1 == "blue" and colour2 == "yellow") or (colour2 == "blue" and colour1 == "yellow"):
        mixed_colour = "green"
    else:
        print("-----------")
        print("Invalid mixing of colours!")

    if mixed_colour:
        print("-----------")
        print("Your mixed color is:", mixed_colour)

else:
    print("Your colour is not a primary colour!")

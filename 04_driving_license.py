age = int(input("Enter your age: "))

if age >= 18:
    cnic = input("Do you have a CNIC? (yes/no): ")
    if cnic.lower() == "yes":
        vehicle_applied = input("Choose a vehicle you applied for: ")
        print("You have chosen for: ", vehicle_applied)

        learning_license_issued = input("Do you have a learning license? (yes/no): ")

        if learning_license_issued.lower() == "yes":
            learning_license_days = int(input("How many days has your licesned been issued for? "))

            if learning_license_days >= 40:
                print("\nYou have been assigned a driving license!")

            else:
                print(f"Please check back in: {40 - learning_license_days} days")
        else:
            print("Please get a learning license first")
    else:
        print("Please get a CNIC first")
else:
    print("Not eligible for a driving license")

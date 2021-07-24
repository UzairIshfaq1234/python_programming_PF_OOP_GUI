class login:
    def __init__(self):
        self.data={}

    def add_data(self):
        self.username=input("Enter your name :")
        self.password=int(input("Enter your Password:"))
        self.data.update({self.username:self.password})
        print("___________________________DATA SUBMITTED!____________________________")

    def login(self):
        self.finduser=input("Enter your Username:")
        self.findpass=int(input("Enter your password: "))
        print("_________________________________________")

        if self.finduser in self.data.keys():
            if self.findpass in self.data.values():
                print("\n")
                print("_________________________________________")
                print(f"DEAR {self.finduser} YOU HAVE ACCESSED!")
                print("_________________________________________")


            else:
                print("\n")
                print("Incorrect password!")

        else:
            print("\n")
            print("Incorrect Username!")

    



person=login()

while True:
    print("PRESS 1 TO ADD DATA!")
    print("PRESS 2 TO LOGIN!")
    print("______________")
    choice=int(input(""))
    print("______________")

    if choice==1:
        person.add_data()

    elif choice==2:
        person.login()

    else:
        print("You pressed incorrect key!")
























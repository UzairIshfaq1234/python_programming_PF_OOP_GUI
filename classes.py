class login:


    def __init__(self,choice):
        self.choice=choice
        self.data={}
    
    #sign in to data
    def datasign(self):
        self.n=input("\t\t     ENTER YOUR NAME     : ")
        if self.n in self.data.keys():
            print("_______________________")
            print("Username already taken!")
            print("_______________________")
            
        else:
            self.p=int(input("\t\t     ENTER YOUR PASSWORD : "))
            self.data.update({self.n:self.p})
            print("\n")
            print("\t\t   ||||||||||||||||||||||||||")
            print("\t\t   _______DATA UPDATED_______")
            print("\t\t   ||||||||||||||||||||||||||")

    #login data all
    def datalogin(self):
        self.username=input("\t\t   ENTER YOUR USERNAME     : ")
        self.password=int(input("\t\t   ENTER YOUR PASSWORD : "))

        if self.username in self.data.keys():
            if self.password in self.data.values():
                print("\n")
                print(f"\t\t  {self.username.capitalize()} YOU GOT ACCESSED!")
                print("\n")
            else:
                print("incorrect password!")
        else:
            print("Incorrect Username!")


        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    def dataall(self):
        print("__________________________________________________________________________________________________")
        print(self.data)
        print("__________________________________________________________________________________________________")


while True:
    print("______________________________________________________________")
    print("______________________WELCOME TO LOGIN SYSTEM_________________")
    print("_______________________PRESS 1 FOR Signup_____________________")
    print("_______________________PRESS 2 FOR Login______________________")
    print("_______________________PRESS 3 FOR Data_______________________")
    print("\n")


    t=int(input("Enter your choice!"))
    p1=login(t)

    if t==1:
        p1.datasign()

    if t==2:
        p1.datalogin()

    if t==3:
        p1.dataall()

    else:
        print("incorrect choice!")


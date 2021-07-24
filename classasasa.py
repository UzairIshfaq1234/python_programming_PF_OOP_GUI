class person:
    def __init__(self,name,roll,cash):
        self.name=name
        self.roll=roll
        self.cash=cash

    def addcash(self):
        self.add=int(input("Enter Amount Want to ADD: "))
        self.cash=self.cash+self.add
        print(f"your cash is:{self.cash}")
        print(f"Dear {self.name} Have Added RS:{self.add} To your account")

    def redcash(self):
        self.less=int(input("Enter Amount want to Deduct: "))
        self.cash=self.cash-self.less
        print(f"Dear {self.name} Have Deducted RS:{self.less} from your account")

    def data(self):
        print(f"Name : {self.name}")
        print(f"Roll : {self.roll}")
        print(f"Cash : {self.cash}")


    #n=input("Enter your name:     ")
    #r=input("Enter your Roll no:  ")
    #c=int(input("Enter your cash: "))

p1=person("uzair","030",100)
while True:
    print("Press 1 to Add cash     ")
    print("Press 2 to Deduct cash  ")
    print("Press 3 to Get all data ")
    print("__________________")
    choice=int(input("Enter your choice:"))
    if choice==1:
        p1.addcash()

    elif choice==2:
        p1.redcash()

    elif choice==3:
        p1.data()

    
    

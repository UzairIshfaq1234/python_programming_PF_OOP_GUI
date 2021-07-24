class person:
    def __init__(self,name,account):
        self.name=name
        self.account=account
        self.store={}

"""    
class open(person):
    def __init__(self, name, account,pin,books):
        self.books=[books]
        self.pin=pin
        super().__init__(name, account)

    def data(self):
        print(f"NAME: {self.name}\nACCOUNT NO:{self.account}\nPIN:{self.pin}\nBOOKS:{self.books}")

while True:
    print("!_______________________________WELCOME_____________________________!")
    n=input("ENTER YOUR NAME: ")
    a=int(input("INPUT YOUR ACCOUNT NUMBER: "))
    b=int(input("ENTER YOUR PIN: "))
    s=input("ENTER BOOKS: ")
    uzair=open(n,a,b,s)
    print("________________________!DATA SUCCESSFULLY ENTERD!______________________")
    choice=int(input("ENTER YOUR CHOICE\n(1):To continue\n(2):Quite"))
    if choice==1:
        
        print("_______________________________________")
        sec=(int(input("ENTER YOUR PIN TO SEE DATA: ")))
        if sec==b:
            uzair.data()
        else:
            print("INCORRECT PIN")
    if choice==2:
        quit

"""



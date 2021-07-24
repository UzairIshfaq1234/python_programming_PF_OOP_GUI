
from random import randint
from inherit1 import person

class open(person):
    def __init__(self, name,books,account,pin):
        self.books=[books]
        self.pin=pin
        super().__init__(name,account)

    def data(self):
        print(f"NAME: {self.name}\nACCOUNT NO:{self.account}\nPIN:{self.pin}\nBOOKS:{self.books}")

while True:
    print("!_______________________________WELCOME_____________________________!")
    n=input("ENTER YOUR NAME: ")
    s=input("ENTER BOOKS: ")
    a=int(input("INPUT YOUR ACCOUNT NUMBER: "))
    p=int(input("ENTER YOUR PIN: "))
    uzair=open(n,s,a,p)
    uzair.store[uzair.pin]=[uzair.name,uzair.account,uzair.books] #saving data in dictunory
    print(f"Your pin is:{uzair.pin}")
    print("________________________!DATA SUCCESSFULLY ENTERD!______________________")
    choice=int(input("ENTER YOUR CHOICE\n(1):To continue\n(2):Quite"))
    if choice==1:
        
        print("_______________________________________")
        sec=int(input("ENTER YOUR PIN TO SEE DATA: "))
        if sec in uzair.store.keys(): #accesiing dictonay by keys
            uzair.data()

        else:
            print("incorrect pin")
        """ 
        if sec==p:
            uzair.data()
        else:
            print("INCORRECT PIN")
        """
    if choice==2:
        quit
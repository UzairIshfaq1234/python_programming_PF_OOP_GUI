class employee:
    def __init__(self):
        self.collection={}

    ######################################----ENTER DATA OF EMPLOYEEE----#################################################
    def enterdata(self):
        print("_________________________________DEAR EMPLOYEE ENTER YOUR CORRECT DATA______________________________")
        self.pin=int(input("Enter your Pin:"))
        self.name=input("Enter your Name: ")
        self.username=input("Enter your Gmail: ")
        self.department=input("Enter your Department: ")
        self.salary=input("Enter your Salary: ")
        print("______________________________________________________________________________________________________________")
        self.n=(f"| Name:  {self.name} | Gmail:{self.username}  |  Department: {self.department}   |   Salary:  {self.salary}")
        self.collection.update({self.pin:self.n})
        #print(self.collection.values())
        print(f"| Name:  {self.name} | Gmail:{self.username}  |  Department: {self.department}   |   Salary:  {self.salary}")
        print("________________________________________________DATA ADDED!___________________________________________________")

    ################################---------UPDATE DATA OF EMPLOYEE-------######################################################

    def update(self):
        print("\n")
        print("___________________________________________UPDATE YOUR DATA HERE_____________________________________")
        self.updater=int(input("Enter your Key pin:"))
        print("_____________________________________________________________________________________________________")
        print(f"________________________UPDATING DATA OF {self.updater()}_____ ____________________________")
        print("_____________________________________________________________________________________________________")
        if self.updater in self.collection.keys():
            self.name=input("Enter your name: ")
            self.username=input("Enter your Gmail:         ")
            self.department=input("Enter your Department: ")
            self.salary=input("Enter your salary:         ")
            self.n=(f"| Name:  {self.name} | Gmail:{self.username}  |  Department: {self.department}   |   Salary:  {self.salary}---|||||---")
            self.collection.update({self.updater:self.n})
            print("\n")
            print(f"____________________{self.name.capitalize()}____YOUR DATA IS UPDATED!__________________")
            print("\n")
        else:
            print("\n")
            print("User name not founnd")


    ################################-----------GET ALL DATA ABOUT COMPANY------------#########################################################3

    def dataall(self):
        print("\n")
        print("_______________________________________________________________________________________________________________")
        print(self.collection)
        print("_______________________________________________________________________________________________________________")
        print("\n")
    def removedata(self):
        print("\n")    
        r=int(input("Enter your key pin to remove data: ") ) 
        self.collection.pop(r) 
        print("_______DATA IS REMOVED_____")

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
p1=employee()
while True:
    print("press 1 to enter data ")
    print("press 2 to update data")
    print("press 3 to see data   ")
    print("Press 4 to remove data")
    print("_______________________________")
    choice=int(input("Enter your choice: "))
    print("_______________________________")

    print("\n")
    if choice==1:
        p1.enterdata()

    elif choice==2:
        p1.update()
    
    elif choice==3:
        p1.dataall()

    elif choice==4:
        p1.removedata()

    else:
        print("\n")
        print("Incorrect selection")

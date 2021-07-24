class person:
    def __init__(self):
        self.name=""
        self.age=""

    def licence(self,age=int(input("ENTER AGE: ")),name=input("ENTER NAME: ")):
        self.name=name
        self.age=age
        if age>=18:
         
            print("_______________________________________________________")
            print("DEAR!",name," YOU ARE ELIGIBLE FOR LICENCE")
            print("_______________________________________________________")
            cnic=int(input("PLEASE! ENTER YOU CNIC NUMBER:\n "))
            self.cnic=cnic
            print("________________________YOUR DATA!_____________________")
            print("NAME: ",self.name)
            print("AGE : ",self.age )
            print("CNIC NUMBER: ",self.cnic)
            print("_______________________________________________________")


        else:
            print("_______________________________________________________")
            print("DEAR!!!",self.name,"YOU ARE NOT ELIGIBLE FOR LICENCE!")
            print("_______________________________________________________")

def main():
    person1=person()
    person1.licence()
    print("________________________PERSON 2______________________")
    person2=person()
    person2.licence()



main()

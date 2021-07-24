class student:
    def __init__(self,name,roll):
        self.collector={}
        self.name=name
        self.roll=roll

    def allinfo(self):
        print(self.collector)

#####################################################################################
class fullinfo(student):
    def __init__(self):
        super().__init__(name=input("enter name:"),roll=input("enter roll: "))

    def datainput(self):
        print("_______________")
        self.dep=input("Enter your department: ")
        self.session=input("Enter your session: ")
        self.k=(f"Name :{self.name} | Roll no : {self.roll} | Department: {self.dep} | Session : {self.session}")
        self.collector.update({self.name:self.k})
        print("________________")
        print("Data Added")

    def allinfo(self):
        print(self.collector)


class teacher(student):
    def __init__(self):
        super().__init__("asfandyar","00321")

    def datainput(self):
        print("_______________")
        self.dep=input("Enter your department: ")
        self.session=input("Enter your session: ")
        self.k=(f"Name :{self.name} | Roll no : {self.roll} | Department: {self.dep} | Session : {self.session}")
        self.collector.update({self.name:self.k})
        print("________________")
        print("Data Added")

    def allinfo(self):
        print(self.collector)



#for teacher
p1=teacher()
p1.datainput()
p1.allinfo()
print("__________________")
p1.allinfo()
#for student
p1=fullinfo()
p1.datainput()
p1.allinfo()
print("__________________")
p1.allinfo()




#p1=student("uzair","030")
#p1.getname()
#p1.getroll()
#print("___________________")
#p1.setname("awais")
#p1.setroll("011")
#p1.getname()
#p1.getroll()
#print("___________________")


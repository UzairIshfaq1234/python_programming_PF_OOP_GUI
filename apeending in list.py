class data:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        self.more=[]

    def printing(self):
        print("__________________________DATA______________________________")
        print("Name :",self.name)
        print("Salary :",self.salary)
        print("Role :",self.role)
    def add_data(self):
       self.more.append(self.printing())


def main():
    for i in range(2):
        n=input("Enter your name?")
        s=int(input("Enter your salary?"))
        r=input("Enter your role?")
        cd=data(n,s,r)
        cd.more.append(cd)

        
    
    
    
  

main()
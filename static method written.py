class employee:
    count=0 #static/class data memeber
    def __init__(self,name):
        self.name=name
        count=+1
    def numberofemployees(): #satatic memeber method
        print("total number of employee in our copmnay is ",employee.count)
    
employee.numberofemployees()
e1=employee("abc")
employee.numberofemployees()
e1=employee("asc")
employee.numberofemployees()





        
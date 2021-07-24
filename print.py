class employee:
    def __init__(self,name,salary,dep):
        self.name=name
        self.salary=salary
        self.dep=dep

    def printinginformation(self):
        print("Name:",self.name)
        print("Salaray:"+self.salary)
        print(f"Department: {self.dep} ")


uzair=employee("M.uzair","1 lac ","BSCS")
uzair.printinginformation()
print("_________________________________________________")
khadija=employee("khadija","1 lac ","BSCS")
khadija.printinginformation()



































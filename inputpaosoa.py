class papa:
    def __init__(self,name):
        self.data=[]
        self.name=name

    #def papaname(self):
    #    self.name=input("Papa Enter your name :")
    #    self.data.append(self.name)

class kid(papa):
    def __init__(self):
        super.__init__(name=input("Enter your papa nmae"))
        
    def kidname(self):
        self.kidn=input("KID enter your name:")
        self.data.append(self.kidn)

    def printdatakid(self):
        print(f"NAME: {self.kidn} {self.name}")


person=kid()
person.kidname()

































class Person:

    def __init__(self, name, cnic, gender, age):
        self.name = name
        self.cnic = cnic
        self.gender = gender
        self.age = age

    def info(self):
        print("Name:", self.name)
        print("CNIC:", self.cnic)
        print("Gender:", self.gender)
        print("Age:", self.age)

class Student(Person):
    
    def __init__(self, name, cnic, gender, age, roll_number):
        self.roll_number = roll_number
        Person.__init__(self, name, cnic, gender, age)

    def info(self):
        Person.info(self)
        print("Roll number:", self.roll_number)

student = Student("Badr", "123456", "M", 15, 12)
student.info()

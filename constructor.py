class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter your name: ")
age = int(input("Enter your age: "))

obj1 = Person(name, age)
print(obj1.name)
print(obj1.age)

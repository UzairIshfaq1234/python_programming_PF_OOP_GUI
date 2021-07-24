class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

person = Person("Badr", 10)

person.set_name("Name")
print(person.name)

person.set_age(20)
print(person.age)

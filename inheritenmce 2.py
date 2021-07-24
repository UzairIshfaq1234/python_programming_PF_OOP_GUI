class Person:
	def __init__(self,name,cnic,gender,age):
		self.name=name
		self.cnic=cnic
		self.gender=gender
		self.age=age
	def info(self):
		print('Name ' ,self.name)
		print('CNIC ' ,self.cnic)
		print('Gender ' ,self.gender)
		print('Age ' ,self.age)
class student(Person):
	def __init__(self,name,cnic,gender,age,roll_no):
		self.roll_no=roll_no
		Person.__init__(self,name,cnic,gender,age)
	def info(self):
		Person.info(self)
		print('roll no ' ,self.roll_no)


def main():
	n=input('enter ur name ')
	c=input('CNIC ')
	g=input('Gender ')
	a=input('Age ')
	r=input('roll no ')
	s1=student(n,c,g,a,r)
	s1.info()

main()
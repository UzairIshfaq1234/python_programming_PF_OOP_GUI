class notebook:
	def __init__(self,name=input("ENTER YOUR SUBJECT!")):
		self.name=name
		self.note=[ ]
		self.note1=""
		self.note2=""
		self.note3=""
		

	def get_note(self):
		return note
	def set_note(self,note1=input("ENTER NOTE 1: "),note2=input("ENTER NOTE 2: "),note3=input("ENTER NOTE 3: ")):
		return self.set_note

	def get_note1(self):
		return self.note1
	def set_note1(self,note1):
		self.note1=note1
		
	def get_note2(self):
		return self.note2
	def set_note2(self,note2):
		self.note2=note2
		
	def get_note3(self):
		return self.note3
	def set_note3(self,note3):
		self.note3=note3


	def get_name(self):
		return name
	def set_name(self,name):
		self.name=name
	def print_data(self,note):
		print("note 1:",self.note1)
		print("note 2:",self.note2)
		print("note 3:",self.note3)
		
oop=notebook()
print(oop.print_data("notes"))

	
		
		
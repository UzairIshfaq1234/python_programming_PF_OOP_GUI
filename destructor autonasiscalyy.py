class demo:
    def insta():
        print("this is stataic method")
    def display(self):
        print("this an instance method")

print("___________________________________________________________")
demo.insta()
#print("___________________________________________________________")
#demo.display("abc")  #self is given 
print("___________________________________________________________")
d=demo()
d.display()

    

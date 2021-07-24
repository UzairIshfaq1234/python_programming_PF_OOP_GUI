from tkinter import *


def log():
			
			if name.get()=="uzair":
				if password.get()=="1234":
					ol=Label(text="ACCESSED!!!!!!!!!!!!!!!!",fg="black",bg="lightgreen")
					ol.place(relx=0.32,rely=0.30)
					nam.delete(0,END)
					pas.delete(0,END)
					
					main_screen=Tk()
					main_screen.configure(width=700,height=1300,background="darkblue")
					main_screen.title("Accesed!! Page")
					#na=Label(text="WELCOME UZAIR TO LGU GUI PAGE",fg="white")
					#na.pack(side=TOP)
					main_screen.mainloop()
				else:
					bl=Label(text="PASSWORD DENIED!",fg="black",bg="red")
					bl.place(relx=0.32,rely=0.30)
					nam.delete(0,END)
					pas.delete(0,END)
				
			else:
				cl=Label(text="INCORRECT NAME!!!",fg="black",bg="red")
				cl.place(relx=0.32,rely=0.30)
				nam.delete(0,END)
				pas.delete(0,END)
	
				
			
			
			
			
			
			
main_window=Tk()
main_window.title("LGU LOGIN!")

#login
na=Label(text="LOGIN",fg="black",bg="white",width=42)
na.place(relx=0,rely=0.03)


#username
nam=Label(text="User Name",fg="black")
nam.place(relx=0.40,rely=0.09)
#username entry
name=StringVar()
nam=Entry(textvariable=name)
nam.place(relx=0.29,rely=0.13)


#password
passwor=Label(text="Password",fg="black")
passwor.place(relx=0.40,rely=0.17)
#passwors entry
password=StringVar()
pas=Entry(textvariable=password)
pas.place(relx=0.29,rely=0.21)




#login
b=Button(text="Login" ,bg="black",fg="white",command=log)
b.place(relx=0.32,rely=0.25)

#quit button
qb=Button(text="Quit",bg="black",fg="white",command=main_window.destroy)
qb.place(relx=0.55,rely=0.25)







main_window.mainloop()
name=[]
passo=[]

while True:
    print("\n")
    print("\n")


    print("______________________________________WELCOME TO LOGIN SYSTEM______________________________")

    
    print("\n")
    print("Press 1 to  Sign in!")
    print("Press 2 to  Login  !")
    print("Press 3 to get all: ")
    print("______________________")
    #taking deatils about 
    x=int(input("Enter your choice : "))

    if x==1:
        u=input("Enter your Gmail   : ")
        name.append(u)
        p=input("Enter your Password: ")
        passo.append(p)
        #uni=input("Enter your University Name: ")
        #roll=input("Enter your roll no: ")
        #sem=input("Enter your Semester: ")
        print("\n")
        print(f"__________________________________DEAR! \"{u.capitalize()}\" YOUR DATA IS ADDED_____________________________")

    if x==2:
        print("_____________________________________LOGIN__________________________________")
        u=input("Gmail    : ")
        p=input("Password : ")
        if u in name:
            if p in passo:
                print(f"DEAR! {u.capitalize()}")
                print("YOU ARE ACCESSED!")

            else:
                print("----DENIED----")
                print("incorrect Password")

        else:
            print("----DENIED----")
            print("Incorrect Username!")

    
    elif x==3:
        print(name)
        print(passo)






































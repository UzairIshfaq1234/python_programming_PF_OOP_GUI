name={}



while True:

    print("______________________________________________________________")
    print("______________________WELCOME TO LOGIN SYSTEM_________________")
    print("_______________________PRESS 1 FOR Signup_____________________")
    print("_______________________PRESS 2 FOR Login______________________")
    print("_______________________PRESS 3 FOR Data_______________________")
    print("\n")
    print("\t\t      ____________________")
    choice=int(input("\t\t\t\t"))
    print("\t\t      ____________________")
    print("\n")
    #signup 
    if choice==1:
        n=input("\t\t     ENTER YOUR NAME     : ")
        if n in name.keys():
            print("_______________________")
            print("Username already taken!")
            print("_______________________")
            
        else:
            p=int(input("\t\t     ENTER YOUR PASSWORD : "))
            name.update({n:p})
            print("\n")
            print("\t\t   ||||||||||||||||||||||||||")
            print("\t\t   _______DATA UPDATED_______")
            print("\t\t   ||||||||||||||||||||||||||")
       

       
    #login
    elif choice==2:
        username=input("\t\t   ENTER YOUR USERNAME     : ")
        password=int(input("\t\t   ENTER YOUR PASSWORD : "))

        if username in name.keys():
            if password in name.values():
                print("\n")
                print(f"\t\t  {username.capitalize()} YOU GOT ACCESSED!")
                print("\n")
            else:
                print("incorrect password!")
        else:
            print("Incorrect Username!")


        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    #printing data
    elif choice==3:
        print("__________________________________________________________________________________________________")
        print(name)
        print("__________________________________________________________________________________________________")

    else:
        print("INCORRECT SUBMITTION")
























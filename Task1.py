while True:
    employee={}

    print("\n")
    print("_____________________________WELCOME TO EMPLOYEE SYSTEM_____________________")
    print("")
    print("PRESS 1: TO LOOK UP AN EMPLOYEE IN THE DICTIONARY")
    print("PRESS 2: ADD A NEW EMPLOYEE TO THE  DICTIONARY   ")
    print("PRESS 3: CHANGE AN EXISTING EMPLOYEE NAME!!, DEPARMENT!!, AND JOB TITLE IN THE DICTIONARY ")
    print("PRESS 4: DELETE AN EMPLOYEE FROM THE DICTIONARY")
    print("PRESS 5: TO QUITE")
    print("_____________________________________________________________________________")
    print("\n")
    choice=int(input("ENTER TO PERFORM ANY ACTION:  "))
    if choice==1:
        #def lookup():
        print("")
        search=int(input("ENTER THE ID OF EMPLOYEE! TO SEARCH!!..... "))
        print(employee[search])
    


    elif choice==2:
        #def addup():
        print("")
        print("_____________________________ENTER EMPLOYEE DATA____________________________")
        id=int(input("ENTER EMPLOYEE ID?  "))
        name=input("ENTER EMPLOYEE NAME!!  ")
        dep=input("ENTER EMPLOYEE DEPARTMENT  ")
        jobtitle=input("INPUT JOB TITLE!!  ")
        data=("NAME: ",name," DEPARTMENT: ",dep,"JOB TITLE: ",jobtitle)
        employee.update({id:data})
    elif choice==4:
        #def clear():
        print("")
        remove=int(input("ENTER THE ID OF EMPLOYEE WHICH YOU WANT TO REMOVE!  "))
        employee.pop(remove)
        print("EMPLOYEE--",remove,"-- HAS BEEN REMOVED!!...........")

    elif choice == 5:
        print("")
        print("THANKS ALLAH HAFIZ.......................................")
        exit()

    else:
        print("WRONG SELECTION!!")

 








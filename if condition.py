print("\n")

name=input("ENTER YOUR NAME: ")
age=int(input("ENTER YOUR AGE: "))
print("________________________________________")

if age>18 and age<80:
    print("DEAR!! "+name+"\nYOUR ARE ELIGIBLE FOR LICENCE")
elif age<18 and age>7:
    print("DEAR!! "+name+"\nYOU ARE NOT ELIGIBLE FOR LICENCE")
elif age==18:
    print("DEAR!! "+name+"\nGET TO NEARIST TRAFFIC POLICE STATION TO GET INFORMATION ")
else:
    print("INCORRECT AGE!! \n ENTER AGE AGAIN")
print("________________________________________")



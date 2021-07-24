
name=[]
passo=[]
u="name"
p="1231"

for i in range(3):
    print("_____________________________________________________________________________________")
    u=input("Enter your Gmail   : ")
    if u in name:
        print("user name taken")
    else:
        name.append(u)
        
    p=input("Enter your Password: ")
    passo.append(p)
    print("__________")

print("_________________________________REMOVING_________________________")
rm=input("User name to remove!")
pm=input("password to remove!")
name.remove(rm)
passo.remove(pm)
print(name)
print(passo)

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

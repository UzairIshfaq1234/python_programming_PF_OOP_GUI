
print("________________________________________")

list1=[input("enter name 1: "),int(input("Enter any number: ")),input("enter name 2: "),int(input("Enter any number: "))]
print("________________________________________")


for item in list1:
    if str(item).isalpha():
        print(item)

print("________________________________________")

for item in list1:
    if str(item).isnumeric() and item<10:
        print(item)

print("________________________________________")

for item in list1:
    if str(item).endswith("ais") :
        print(item)
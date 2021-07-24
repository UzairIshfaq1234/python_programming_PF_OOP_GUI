i=0
while (True):
    num1=int(input("Entere number :::"))
    if num1>=100:
        print("congrates you reached 100 above")
        i=i+1
        break

    if num1<100:
        print(num1)
        i=i+1
        continue
    i=i+1

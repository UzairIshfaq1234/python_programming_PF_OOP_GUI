sales = float(input("Please enter total sales in this month: "))

if sales >= 50000:
    bonus = 500.0
    commission_rate = 0.12

    commission = sale * commission_rate

    print("Total commission: ", commission)
    print("Bonus: ", bonus)
    print("_______________")
    print("Total Payable Amount: ", commission + bonus)

print("Thank you!")

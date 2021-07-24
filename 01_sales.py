sales = float(input("Please enter total sales in this month: "))

bonus = 0
commission_rate = 0
commission = 0

if sales >= 50000:
    bonus = 500.0
    commission_rate = 0.12

if sales < 50000:
    bonus = 200.0
    commission_rate = 0.10

commission = sales * commission_rate
    
print("Total Commission: ", commission)
print("Your Bonus: ", bonus)
print("* -------------- * ")
print("Total Payable Amount: ", commission + bonus)

print("---- Thank you! ----")

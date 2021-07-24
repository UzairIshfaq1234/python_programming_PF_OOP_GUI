loan = int(input(("Enter monthly cost for loan payment: ")))
insurance = int(input(("Enter monthly cost for insurance: ")))
gas = int(input(("Enter monthly cost for gas: ")))
oil = int(input(("Enter monthly cost for oil: ")))
tires = int(input(("Enter monthly cost for tires: ")))
maintenance = int(input(("Enter monthly cost for maintenance: ")))


monthly_cost = loan + insurance + gas + oil + tires + maintenance

annual_cost = monthly_cost * 12

print("Monthly cost for the expenses: ", monthly_cost)
print("Annaul cost for the expenses: ", annual_cost)

weight_of_package = int(input("Enter weight of the package in pounds: "))


if weight_of_package > 2 or weight_of_package <= 6:
    rate_per_pound = 2.20

elif weight_of_package > 6 or weight_of_package <= 10:
    rate_per_pound = 3.70

elif weight_of_package > 10:
    rate_per_pound = 3.80

else:
    rate_per_pound = 1.10

shipping_charges = weight_of_package * rate_per_pound

print("--------")
print("Shipping charges: ", shipping_charges)

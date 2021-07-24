def get_values():

    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))

    return weight, height

def calculation(weight, height):

    bmi = (weight * 703) / (height * height)

    print("BMI: ", round(bmi, 2))

    return bmi

def scale(bmi):

    if bmi < 18.5 and bmi >= 0:
        print("Underweight")
    elif bmi <= 24.9 and bmi >= 18.5:
        print("Normal weight")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")
    else:
        print("Invalid BMI")

def main():
    weight, height = get_values()

    bmi = calculation(weight, height)

    scale(bmi)

main()

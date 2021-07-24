def calculate_hours():
    hours = int(input("How many hours have you worked? "))
    hourly_pay_rate = float(input("Enter your hourly pay rate: "))

    return hours, hourly_pay_rate

def calculate(hours, hourly_pay_rate):
    if hours > 40:
        extra_hours = hours - 40
        extra_hours_pay = hourly_pay_rate * 1.5
        forty_hour_pay = 40 * hourly_pay_rate
        extra_pay = extra_hours * extra_hours_pay 

        gross_pay = forty_hour_pay * extra_pay

    else:
        gross_pay = hours * hourly_pay_rate
    
    return gross_pay

hours, hourly_pay_rate = calculate_hours()

gross_pay = calculate(hours, hourly_pay_rate)

print("Your gross pay is: ", gross_pay)

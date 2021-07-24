minute = 60
hour = 3600
day = 86400

seconds = int(input("Enter the number of seconds: "))

if seconds >= 0 and seconds < minute:
    print("The time in seconds is", seconds)

elif seconds >= minute and seconds < hour:
    minutes = int(seconds / minute)

    print("The time in minutes is", minutes)

elif seconds >= hour and seconds < day:
    hours = int(seconds / hour)

    print("The time in hours is:", hours)

elif seconds >= day:
    days = int(seconds / day)

    print("The time in days is:", days)

else:
    print("Time cannot be negative!")

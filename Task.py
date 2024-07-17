# income = 85528
#
# if income<=85528:
#     tax = income*0.18-556.02
# else:
#     tax= 14839.02 + (income-85528)*0.32
#     return max(0, round(tax))


year = int(input("Enter the year: "))

# Check if the year is within the Gregorian calendar period
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Check if it's a leap year or a common year
    if (year % 4 != 0):
        print("Common year")
    elif (year % 100 != 0):
        print("Leap year")
    elif (year % 400 != 0):
        print("Common year")
    else:
        print("Leap year")






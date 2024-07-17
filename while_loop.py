def addition():
    num1 = int(input("Enter first  number:"))
    num2 = int(input("Enter second number:"))
    result = num1 + num2
    print(result)


def subtraction():
    num1 = int(input("Enter first  number:"))
    num2 = int(input("Enter second number:"))
    result = num1 - num2
    print(result)


def multiplication():
    num1 = int(input("Enter first  number:"))
    num2 = int(input("Enter second number:"))
    result = num1 * num2
    print(result)


def Divison():
    num1 = int(input("Enter first  number:"))
    num2 = int(input("Enter second number:"))
    result = num1 / num2
    print(result)
    print("the results are", result)


while (1):
    choice = int(input("Enter your choice:"))
if (choice == 1):
    addition()
elif (choice == 2):
    subtraction()
elif (choice == 3):
    multiplication()
elif (choice == 4):
    Divison()
else:
    exit(0)







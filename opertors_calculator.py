num1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator!")

print("Result:", result)



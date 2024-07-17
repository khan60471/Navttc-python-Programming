#this is the practice of seperation functions
print("abdullah", end =  " ")
print("khan")
print("abdullah", sep="-" ,end= " ")
print("khan")
print("abdullah", sep="_ ")
print("khan")
print("abdullah \n khan \n 20 ")
print("abdullah\nkhan\n20 ")


print("my" "name" "is" , sep="_" , end="*")
print("khan")
print("\"I'm\"" , "\"\"Learning\"\"" , "\"\"\"python\"\"\"\"", sep="\n" )

#savings = 100
#total_savings = 200
#print("i'm starting with $" + str(savings) + " and now i have $"+ str(total_savings) + " Awesome!")  

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
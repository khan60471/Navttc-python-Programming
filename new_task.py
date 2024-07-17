
def  addition():
    num1 = int(input("Enter first  number:"))
    num2 = int(input("Enter second number:"))
    result  = num1 + num2
    print(result)

def  subtraction():
    num1 = int(input("Enter first  number:"))
    num2 = int(input("Enter second number:"))
    result  = num1 - num2
    print(result)

choice = int(input("Enter your choice:"))
if choice==1:
        addition()
else:
        subtraction()
    
        
    
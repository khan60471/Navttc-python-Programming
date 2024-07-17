height = int(input("Enter your height in cm:"))
age = int(input("enter your age:"))
bill = 0
if height > 120:
    print("ride")
    if age < 12:
     print("you have to pay 5$")
     bill = 5
    elif age <18:
       bill = 7
       print("you have to pay 7$")

    else:
        bill = 12
        print("you have to pay 12$") 

    wants_photo = input("Do you want a photo? Y or N: ")
    if wants_photo =="Y":
      bill+=3
      print(f"your final bill is {bill}")
    

else:
    print("can't ride")
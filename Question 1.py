age= int(input("Enter Your Age: "))
if age >= 18:
    print("You are eligible to vote!")
    
elif age <= 0:
    print("Age cannot be negative or zero")
    
else:
    print('You are not eligible to vote!')
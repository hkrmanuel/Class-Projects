import math as m

def pythagurus(a, b):
    result = m.sqrt(a**2+b**2)
    print("The value of Hypotenus is", result)
    
a = int(input("Enter the first short side: "))
b = int(input("Enter the Second short side: "))

pythagurus(a, b)
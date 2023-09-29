add = 0
avg =0
n =0

while True:
    
    user = int(input("Enter Value To Acquire the Average or input Zero to end:"))
    
    add += user
    print(add)

    n += 1
    
    
    
    if user == 0 and add != 0:
        avg = float(add/(n-1))
        print("The Average Of THe values is", avg)
        break
    if user == 0 and add == 0:
        print("Average Cannot be Cummulated")
 
    
    
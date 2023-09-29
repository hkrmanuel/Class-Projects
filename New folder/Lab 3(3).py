sides =[]

for r in range(3):
    x = int(input("Enter Length of  sides:"))
    sides.append(x)
    
if sides[0] == sides[1] == sides[2]:
    print("THis is an Equiateral triangle")
    
elif sides[0] == sides[1] != sides[2] or sides[0]== sides[2] != sides[1] or sides[1] == sides[2] != sides[0]:
    print("THis Is An Isosceles triangle")
    
elif sides[0] != sides[1] != sides[2]:
    print("THis is a Scalene Triangle")
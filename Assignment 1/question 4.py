import math

radius = int(input("Enter The Radius OF the Cylinder:"))
height = int(input("Enter The Height OF the Cylinder:"))
pie= math.pi
area = pie * (radius**2)
volume = area* height 

result= round((volume), 1)
print(result) 
Ta = int(input("Enter The Air Temperature in Degree Celsius:"))
V= int(input("Enter THe Wind Speed In Kilometres per Hour:"))
WCI = 13.12 + (0.6215*Ta) - (11.37)* (V**0.16 ) + (0.3965*Ta)*(V**0.16)
print ("The Wind Chill Index is:",round(WCI))
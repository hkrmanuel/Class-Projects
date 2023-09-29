def celcius_to_farenheit(celcius):
    result = celcius * 9/5 + 32
    print(celcius, "celcius is equal to ", result, "Fahrenheit")

celcius = float(input("Enter Celcius:"))

celcius_to_farenheit(celcius)
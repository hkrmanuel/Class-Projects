def calculator(base, expo):
    result = base ** expo
    print(base, "raised to the power", expo, "is", result)

base = int(input("Input Base:"))
expo= int(input("Input Exponent:"))
calculator(base, expo)
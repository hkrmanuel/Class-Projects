percent = int(input("Enter Your Percentage:"))

if 85 <= percent <= 100:
    print("A+ : Excellent")
elif 80 <= percent <= 84:
    print("A : Excellent")
elif 75 <= percent <= 79:
    print("B+ : Very Good")
elif 70 <= percent <= 74:
    print("B : Very Good")
elif 65 <= percent <= 69:
    print("C+ : Good")
elif 60 <= percent <= 64:
    print("C : Satisfactory")
elif 55 <= percent <= 59:
    print("D+ : Pass")
elif 50 <= percent <= 54:
    print("D : Pass")
elif percent < 50:
    print("E: Fail")

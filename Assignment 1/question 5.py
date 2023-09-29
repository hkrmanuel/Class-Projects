deposit = int(input("Enter Amount Being deposited"))
rate = 4/100
balance = deposit

for y in range(1,4):
    interest = rate * balance
    balance += interest
    print("The Amount in the savings account after", y, "years  is", balance)

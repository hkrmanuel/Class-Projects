deposit = int(input("Enter Amount Being deposited"))
balance = 0
rate = 4/100
year1 = rate * deposit
balance = year1+deposit 
print("The Amount Of Savings after 1 year is", balance, "cedis")
year2 = rate * balance
balance += year2
print ("The amount of savings after 2 year is ", balance," cedis ")
year3= rate* balance
balance += year3
print ( " The amount of saving after 3 years is" , balance ," cedis ")




numbers = []
for r in range(3):
    x = int(input("Enter Number:"))
    numbers.append(x)

arrange = []
arrange.append(min(numbers))
arrange.append(int((max(numbers)- min (numbers))/2 + min(numbers)) )
arrange.append(max(numbers))

print(arrange)
def blank(x,y):
    user = input("Enter Value:")
    if user == "" and y==0:

        return 0
    elif user =="" and y==1:
        return x
    else:
        sum = int(user) + x
        return blank(sum, 1)
print(blank(0,0))
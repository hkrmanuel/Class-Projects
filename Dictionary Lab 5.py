def digits(i):
    my_dict= dict()
    for s in i:
        if s in my_dict:
            my_dict[s] += 1
        elif s == ".":
            m =0
        else:
            my_dict[s] = 1
    return my_dict
print(digits(str(1.322)))
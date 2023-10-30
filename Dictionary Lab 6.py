def unique(i):
    my_dict= dict()
    for s in i:
        if s in my_dict:
            my_dict[s] += 1
        else:
            my_dict[s] = 1
    return len(my_dict)
print(unique("zzzjcd"))
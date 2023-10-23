t = [1,6,4]
def has_duplicates(x):
    n = 0
    m = 0
    for i in x:
        if x[n] == i:
            m +=1
            n += 1
    if m >1:
        return True
    else: 
        return False
print(has_duplicates(t))
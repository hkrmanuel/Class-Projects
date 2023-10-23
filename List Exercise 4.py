t = [1, 2, 3, 4,]
def chop(x):
    x.pop(0)
    x.pop(len(x)-1)
    return x

print(chop(t))
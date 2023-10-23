t = [1, 4, 5]
def is_sorted(x):
    new = []
    for i in x:
        new.append(i)
        
    new.sort()
    if x != new:
        return False
    else:
        return True

print(is_sorted(t))
    
    
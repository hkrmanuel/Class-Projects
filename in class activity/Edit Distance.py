def edistance(s,t):
    global d1, d2,  d3
    if len(s)== 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[-1] != t[-1]:
            cost = 1 
            d1 = edistance(s[:-1], t) + 1
            d2 = edistance(s, t[:-1]) + 1 
            d3 = edistance(s[:-1], t[:-1]) + cost
        
        return min(d1, d2, d3)

print(edistance("forend", "jesus"))
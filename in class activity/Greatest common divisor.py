def gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        
        return gcd(b, c)
    
result = gcd(138, 500)
print(result)
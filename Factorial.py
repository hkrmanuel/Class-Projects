def factorial(n):
    result =0
    if n == 0:
        return 1
    else :
        result = n * factorial(n-1)
            
        return result
    
add = factorial(5)
print(add)
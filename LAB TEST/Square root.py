import math

def mysqrt(a, x):
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
            break
            
        x = y
        
       
        
def test_square_root(a,x):
    print("a | mysqrt(a) | math.sqrt(a)| diff |")
    sqrt = math.sqrt(a)
    mysqrt(a, x)
    
    diff = sqrt - mysqrt(a, x)
    print(a, "|", mysqrt(a,x),"      |", sqrt, "        |", diff , " |")
    
test_square_root(4, 3)

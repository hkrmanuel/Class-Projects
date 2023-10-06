def horiz():
    space = 4
    print("+", "-" * space, "+", "-" * space, "+", "-" * space, "+")
    
def vert():
    space= 4
    for s in range(space):
        print('|', " " * space, '|', " " * space,"|"," " * space,"|" )
        
horiz()
vert()
horiz()
vert()
horiz()
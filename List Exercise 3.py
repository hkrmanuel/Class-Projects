t = [ 1, 2, 3, 4]
def middle(x):
    new_list= []
    for i in x[1:len(x)-1]:
        new_list.append(i)
    return new_list

print(middle(t))
        
    
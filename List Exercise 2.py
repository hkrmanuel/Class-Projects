list = [1, 2, 3]
def cumsum(x):
    new_list = []
    n =0
    for i in x:
       n += i
       new_list.append(n)
    return new_list
print(cumsum(list))
        
''' Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t) '''

t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(lst):
    total = 0
    for i in lst:
        for j in i:
            total += j

    return total
print(nested_sum(t))
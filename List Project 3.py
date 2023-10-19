xs = [2, 3, 4]
def sum_of_squares(xs):
    sum = 0
    for s in xs:
        square = s**2
        sum += square
    return sum
print(sum_of_squares(xs))
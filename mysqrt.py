def mysqrt(a, x):
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            return y
            break
        x = y
mysqrt(4, 3)

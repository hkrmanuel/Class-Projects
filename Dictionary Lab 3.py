def OddEvenCount(i):
    odd = 0
    even = 0
    for s in i:
        if s % 2 == 0:
            even += 1
        elif s % 2 !=0:
            odd += 1
    new_dict = {"odd" : odd, "even": even}
    return new_dict

print(OddEvenCount([1, 3, 4, 5, 6, 7, 8, 9]))

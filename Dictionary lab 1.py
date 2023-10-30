def count(s):
    alpha = dict()
    for j in s:
        if j in alpha:
            alpha[j] += 1
        else:
            alpha[j] = 1
    return alpha

k = input('Enter A Word:')
print(count(k))
pi = "3.1415926535897932384626433832795028841971693993751"
my_dict = dict()
for i in range(len(pi)):
    if pi[i] in my_dict:
        my_dict[pi[i]] += 1
    else:
        my_dict[pi[i]] = 1       
print(my_dict)
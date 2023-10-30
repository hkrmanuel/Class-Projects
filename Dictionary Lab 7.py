def anagrams(s1,s2):
    dict1= dict()
    dict2= dict()
    for x in s1:
        if x in dict1:
            dict1[x] += 1
        else :
            dict1[x] = 1
    for f in s2:
        if f in dict2:
            dict2[f] += 1
        else :
            dict2[f] = 1
    return dict1 == dict2
print(anagrams("james","majes"))
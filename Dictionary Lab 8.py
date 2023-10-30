def anagrams(s1,s2):
    dict1= dict()
    dict2= dict()
    for x in s1.lower():
        if x in dict1:
            dict1[x] += 1
        elif "" in x:
            pass
        else :
            dict1[x] = 1
    for f in s2.lower():
        if f in dict2:
            dict2[f] += 1
        elif "" in x:
            pass
        
        else :
            dict2[f] = 1
    return dict1 == dict2
print(anagrams("james is a man","is a man Majes"))
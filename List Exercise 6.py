t = "hippotamus"
n = "pot"
def is_anagram(x, y):
    if y in x or x in y:
        return True
    else:
        return False

print(is_anagram(t, n))
def cypher(word, n):
    new_word =''
    for s in word:
        index = ord(s) + 3
        new_word += chr(index)
    print(new_word)
cypher("abc", 3)
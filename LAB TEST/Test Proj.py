import math

def cypher(word, b):
    new_word = ''
    for c in word:
        no = ord(c) + b
        new_letter = chr(no)
        new_word += new_letter
    return new_word

jj = cypher("jake", 3)
print(jj)
        
        
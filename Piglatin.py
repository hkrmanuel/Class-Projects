def pig_latin(word):
    if word[0] in "aeiou":
        piglatin = word + "way"    
    else:
        const = ''
        a= 0
        for c in word:
            if c not in "aeiou" and a == 0:
                const += c 
            elif c in "aeiou":
                    a = 1
            piglatin = word[len(const):] +const + "ay"
    print(piglatin)
    return piglatin
pig_latin("pig")
                
            
        
            
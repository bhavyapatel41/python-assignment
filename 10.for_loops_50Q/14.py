sentence = input("Enter sentence: ")
word=sentence.split()
vowel=0
consonant=0
for i in word:
    for j in i:
        if j in "aeiouAEIOU":
            vowels+=1
        elif j>'A' and j<'Z' or j>'a' and j<'z':
            consonants+=1
    if vowel>consonants:
        print(f"{i} vowels win",vowel)
    elif consonants>vowel:
        print(f"{i} consonants win",consonants)
    else:
        print(f"{i} Draw")        

        
       
       

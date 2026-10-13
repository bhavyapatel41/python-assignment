sentence=input("Enter sentence : ")
vowel=0
consonants=0
for i in sentence:
    if i in "aeiouAEIOU":
        vowel+=1
    elif i>'A' and i<'Z' or i>'a' and i<'z':
        consonants+=1

if vowel>consonants:
    print("vowels win",vowel)
elif consonants>vowel:
    print("consonants win",consonants)
else:
    print("Draw")

print(vowel,len(sentence))
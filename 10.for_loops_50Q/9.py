string=input("ENter string : ")
vowel=0
consonant = 0
digit = 0
special = 0

for i in range(1,len(string)):
    print("Position:", i)
    if i % 2 == 0:
        print("position Even")
    else:
        print("position odd")

    char=string[i]
    print("Character : ",char)

    if char in "AEIOUaeiou":
        print("vowel")
        vowel+=1
    elif char>'A' and char<'Z' or char>='a' and char<='z':
        print("consonant")
        consonant+=1
    elif char >= '0' and char <= '9':
        print("digits")
        digit += 1
    else:
        print("special character ")
        special += 1
    
print(f"vowels {vowel},consonants {consonant},digits {digit} , special character {special}")
    
    

   
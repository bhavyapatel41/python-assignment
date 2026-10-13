#largest ,smallest word left
sentence=input("Enter a sentence : ")
words=sentence.split()
num_word=len(words)
print("number of words : ",num_word)
char_num=0
beg_vowel=0
end_vowel=0
digit=False
for i in words:

    for ch in i:
        char_num+=1
        if ch >= '0' and ch <= '9':
            digit+=1  

    if i[0] in "aeiouAEIOU":
        beg_vowel+=1
    if i[-1] in "aeiouAAEIOU":
        end_vowel+=1



print(char_num,"chat count")
print(digit,"digit")
print(beg_vowel,"big vowel")
print(end_vowel,"end vowel")
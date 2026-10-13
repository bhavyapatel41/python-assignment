word1=input("Enter word 1 : ")
word2=input("Enter word 2 : ")
# shorter = max(len(word1), len(word2))

for i in range(len(word1)):
    ch1=word1[i]
    ch2=word2[i]
    
    if ch1==ch2:
        print("S",end="")
    else:
        print("D",end="")    
    
    

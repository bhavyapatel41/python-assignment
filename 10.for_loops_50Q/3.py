sentence=input("Enter sentence : ")
word=sentence.split()

highest_score=0
h_word=""
for j in word:
    score=0
    for i in j:
        if i in "aeiouAEIOU":
            score+=2
        elif i>='A' and i<='Z' or i>='a' and i<='z':
            score+=1
        elif i>='0' and i<='9':
            score+=3
        else:
            score+=4
    print(f"{j} : {score}")

    if score>highest_score:
        highest_score=score
        h_word=j



print(highest_score,h_word)



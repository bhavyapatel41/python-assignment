sentence=input("Enter sentence : ")
words=sentence.split()

for i in range(len(words)):
    # print(i,words[i])
    equal=words[0]
    for j in words:
        if equal==j:
            print(j)



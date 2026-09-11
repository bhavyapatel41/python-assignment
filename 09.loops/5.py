#E. String Iteration

#21

string=input("Enter string : ")

for i in string:
    print(i)

#22
for i in string:
    print(i,end=" ")

#23
count=0
for i in string:
    count+=1
print("Letters in string : ",count)

#24
c=0
for i in string:
    if i=="a":
        c+=1
print("\"a\" in string : ",c)

#25
for i in string:
    if i>='A'and i<='Z':
        print("UpperCase Character : ",i)


#21
string=input("enter a string : ")
i=0
while i<len(string):
    print(string[i])
    i+=1
print("\n")
#22
i=0
while i<len(string):
    print(string[i],end=" ")
    i+=1
print("\n")

#23
i=0
count=0
while i<len(string):
    count+=1
    i+=1
print(count)
print("\n")

#24
i=0
count=0
while i<len(string):
    if string[i]=="a":
        count+=1
    i+=1
print("count \"a\" :",count)
print("\n")

#25
i=0
uppercase_count=0
while i<len(string):
    if string[i]>='A' and string[i]<='Z':
        uppercase_count+=1
    i+=1
print(uppercase_count)

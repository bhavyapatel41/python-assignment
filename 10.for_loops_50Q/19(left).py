sentence=input("Enter a security scanner sentence : ")
words=sentence.split()
uppercase = False
lowercase = False
digit=False

special_chars="!@#$%^&*()_+-:;<>?/"

url=False
at=False


# for i in range(len(sentence)):
#     ch=sentence[i]

#     if ch>='0' and ch<='9':
#         digit=True
#     elif ch >= "A" and ch <= "Z":
#         uppercase = True
#     elif ch >= "a" and ch <= "z":
#         lowercase = True
#     elif ch in special_chars:
#         special = True
    
#     if ch==".":
#         url=True
#     if ch=="@":
#         at=True
        

for w in sentence:
    
    for ch in words:
        if ch>='0' and ch<='9':
         digit=True
        elif ch >= "A" and ch <= "Z":
            uppercase = True
        elif ch >= "a" and ch <= "z":
            lowercase = True
        elif ch in special_chars:
            special = True




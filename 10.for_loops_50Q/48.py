
for i in range(1,10):
    username=input("Enter username : ")
    letter=0
    digits=0
    space=0
    underscore=0
    special_ch=0
    for j in username:
        length=len(username)
        if j>='A' and j<='Z' or j>='a' and j<='z':
            letter+=1
        elif j>='0' and j<='9':
            digits+=1
        elif j=="_":
            underscore+=1
        elif j==" ":
            space+=1
        else:
            special_ch+=1



if space>0:
    print("invalid")
elif special_ch==0:
    print("acceptable")
else:
    print("clean")

print(f"Username : {username}, Letters : {letter}, Digits : {digits}, Spaces : {space}, Underscore : {underscore}, Special : {special_ch}, Length : {length}")

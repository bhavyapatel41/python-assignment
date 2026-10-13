password=input("Enter password : ")

for i in password:
    
    if i in "aeiouAEIOU":
        i="@"
    elif i>='A' and i<='Z' or i>'a' and i<'z':
        i=i.lower()
    elif i>='0' and i<='9':
        i="#"
    elif i==" ":
        i="_"
    else:
        i="!"

    print(i,end="")


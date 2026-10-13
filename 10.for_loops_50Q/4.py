password=input("Enter password : ")
status=0
uppercase=False
lowercase=False
digit=False
special=False
if len(password)>=8:
    status+=1
for i in password:

    if i>='A' and i<='Z' and uppercase==False:
        uppercase=True
        status += 1
        
    elif i>='a' and i<='z' and lowercase==False:
        lowercase=True
        status += 1
        
    elif i>='0' and i<='9'and lowercase==False:
        digit=True
        status += 1
      
    else:
        special=True
        status += 1
        

if status >= 5:
    print("Strong")
elif status >= 3:
    print("Medium")
else:
    print("Weak")

print(status)
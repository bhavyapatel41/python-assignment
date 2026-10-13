string=input("Enter string with letters, digits, spaces, and special characters.")
uppercase=0
lowercase=0
space=0
digit=0
special_character=0
for i in string:
    if i>='A' and i<='Z':
        uppercase+=1
    elif i>='a' and i<='z':
        lowercase+=1
    elif i==" ":
        space+=1
    elif i>='0' and i<=9:
        digit+=1
    else:
        special_character+=1



print(uppercase,lowercase,space,digit,special_character)


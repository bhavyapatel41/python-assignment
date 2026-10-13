code=input("Enter code : ")
uppercase=0
digit=0
if len(code)==8:

        for i in range(0,3):
            if code[i] >='A' and code[i]<='Z':
                uppercase+=1
        for i in range(3,8):
            if code[i]>='0' and code[i]<='9':
                digit+=1
        if uppercase==3 and digit==5:
            print("valid code")
        else:
            print("invalid code")
else:
    print("invalid code")


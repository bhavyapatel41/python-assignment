
for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(2*i-1):
        #print(k,end="")
        if k%2==0:
            print("E",end="")
        else:
            print("O",end="")
        if k%3==0:
            print("T",end="")
        if k%3==0 and k%5==0:
            print("F",end="")
       
        
    print()
for i in range(1,10):
    for j in range(1,i+1):
        if i%2!=0: 
            if j%3==0:
                print("X",end=" ")
            elif j%5==0:
                print("Y",end=" ")
            else:
                print(j,end=" ")
        
    print()



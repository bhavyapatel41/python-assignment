n=int(input("Enter n : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        num=i*j
        # print(num,end=" ")
        if num%2==0:
            print("E",end=" ")
        else :
            print("O",end=" ")
        if num%5==0:
            print("F",end=" ")
            
    print()
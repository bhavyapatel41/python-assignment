# for i in range(4):
#     for j in range(4):
#         print(f"({i},{j})",end=" ")
#     print()



even=0
odd=0
sum_1=0
sum_2=0

for i in range(4):
    for j in range(4):
        num=int(input(f"({i},{j}) : "))
        sum=0
        if i==j:
            sum_1+=num
            if num%2==0:
                even+=1
        if i+j==3:
            sum_2+=num
            if num%2==1:
                odd+=1

print(f"Main diagonal sum {sum_1}\nSecondary diagonal sum {sum_2}\n Number of even values on the main diagonal. {even}\nNumber of odd values on the secondary diagonal. {odd}")           

if sum_1 > sum_2:
    print("Main diagonal sum is greater")
elif sum_2 > sum_1:
    print("Secondary diagonal sum is greater")
else:
    print("Both diagonal sums are equal")
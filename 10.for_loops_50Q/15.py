highest_num=0
even_count=0
odd_count=0
positive_count=0
negative_count=0
zero_count=0
for i in range(1,4):
    for j in range(1,4):
        num=int(input(f"Enter num {i}*{j} : "))
        if num%2==0:
            print(f"{num} is even")
            even_count+=1
        else :
            print(f"{num} is odd")
            odd_count+=1
        if num>0:
            print(f"{num} is positive")
            positive_count+=1
        elif num<0:
            print(f"{num} is negative")
            negative_count+=1
        else:
            print(f"{num} is zero")
            zero_count+=1
        

        if num>highest_num:
            highest_num=num
            

print("Highest number : ",highest_num)

print(f"even {even_count} ,odd {odd_count} ,positive {positive_count},negative {negative_count},zero count {zero_count}")
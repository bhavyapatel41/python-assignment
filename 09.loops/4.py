#D. Calculation Problems

#16
n=int(input("Enter n : "))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"Sum : {sum}")

#17
sum_even=0
for i in range(2,n+1,2):
    sum_even+=i
    
print(f"Sum even: {sum_even}")

print("\n")
#18
sum_odd=0
for i in range(1,n+1,2):
    sum_odd+=i
    
print(f"Sum odd: {sum_odd}")
print("\n")
#19

a=int(input("Enter number : "))
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")

print("\n")
#20
n1=int(input("Enter n : "))
multi=1
for i in range(1,n1+1):
    multi*=i

print(f"multiplication : {multi}")


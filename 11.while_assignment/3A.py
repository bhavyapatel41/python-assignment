#16
n=int(input("Enter n : "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)
print("\n")
#17
i=1
sum=0
while i<=n:
    if i%2==0:
        sum+=i
    i+=1
print("even sum",sum)
print("\n")
#18
i=1
sum=0
while i<=n:
    if i%2==1:
        sum+=i
    i+=1
print("odd sum",sum)
print("\n")
#19
i=1
while i<=10:
    print(f"{n}*{i} = {n*i}")
    i+=1

#20
i=1
multi=1
while i<=n:
    multi*=i
    i+=1
print(multi)
print("\n")
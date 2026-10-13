#11
n=int(input("Enter n : "))
i=2
while i<=n:
    print(i,end=" ")
    i+=2
print("\n")
#12

i=1
while i<=n:
    print(i,end=" ")
    i+=2
print("\n")

#13
i=1
while i<=n:
    if i%3==0:
        print(i,end=" ")
    i+=1
print("\n")

#14
i=1
while i<=n:
    if i%3==0 and i%2==0:
        print(i,end=" ")
    i+=1
print("\n")

#15
i=1
count=0
while i<=n:
    if i%2==0:
        count+=1
    i+=1
print(count)
print("\n")
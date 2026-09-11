#B. range() Practice

#6
for i in range(2,21,2):
    print(i,end=" ")
print("\n")
#7
for i in range(1,20,2):
   print(i,end=" ")
print("\n")
#8
for i in range(3,19,3):
    print(i,end=" ")

print("\n")
#9
for i in range(20,1,-2):
    print(i,end=" ")
print("\n")
#10
number=int(input("enter positive number : "))
for i in range(1,number+1):
    print(i,end=" ")
print("\n")

#C. Conditions with for

#11
for i in range(2,number+1,2):
    print(i,end=" ")

print("\n")

#12
for i in range(1,number+1,2):
    print(i,end=" ")
print("\n")

#13
for i in range(1,number+1):
    if i % 3 == 0:
        print(i,end=" ")
print("\n")
#14
for i in range(1,number+1):
    if i%2==0 and i%3==0:
            print(i,end=" ")
print("\n")
#15
count=0
for i in range(1,number+1):
    if i%2==0:
        count+=1

print(f"even count : {count}")

print("\n")


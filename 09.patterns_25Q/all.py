#1
for i in range(1,4):
    for j in range(1,4):
        print("*",end=" ")
    print()

#2
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()

#3
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()

#4
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
print("\n")

#5
n=5
for i in range(1,n+1):
    for j in range((n+1)-i):
        print("*",end=" ")
    print()

#6
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("\n")

#7
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("\n")

#8
# for i in range(1,6):#table-1 to 5
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()

#9
for i in range(1,4):
    for j in range(1,6):
        print(i*j,end=" ")
    print()
print("\n")

#10
for i in range(1,6):
    for j in range(1,6):
        print(j*j,end=" ")
    print()

#11
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
print("\n")

#12
for i in range(6):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()

#13
for i in range(1,6):
    a=1
    for j in range(i):
        print(a,end=" ")
        a+=2
    print()
print("\n")
#14
for i in range(1,6):
    a=2
    for j in range(i):
        print(a,end=" ")
        a+=2
    print()

#15
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

#16
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

#17
a=1
for i in range(1,4):
    
    for j in range(1,4):
        print(a,end=" ")
        a+=1
    print()

#18
a=1
for i in range(4):
    
    for j in range(5):
        print(a,end=" ")
        a+=1
    print()

#19
for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})",end=" ")
    print()
print("\n")

#20
for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})")

#21

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} ={i*j}")
#     print()

#22
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

print("\n")


#23
n1=5
for i in range(n1):
    for j in range(1,(n1+1)-i):
        print(j,end="")
    print()
print("\n")
#24
for i in range(1,6):
    a=5
    for j in range(6-i):
        print(a,end="")
        a-=1
    print()

        

print("\n")
#25
for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()


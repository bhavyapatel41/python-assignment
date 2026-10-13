#26

i=0
while i<3:
    j=0
    while j<4:
        print("*",end="")
        j+=1
    i+=1
    print()
print("\n")
#27

i=0
while i<4:
    j=0
    while j<5:
        print("*",end="")
        j+=1
    i+=1
    print()

print("\n")
#28

i=0
while i<5:
    j=0
    while j<=i:
        print("*",end="")
        j+=1
    i+=1
    print()

print("\n")
#29

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    i+=1
    print()

#30
i=1
while i<=5:
    j=1
    while j<=10:
        print(f"{i} * {j} = {i*j}")
        j+=1
    i+=1
    print()
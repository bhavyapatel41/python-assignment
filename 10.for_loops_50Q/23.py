total=0
j=0
m=0
s=0
e=0
for i in range(1,9):
    salary=float(input(f"Enter salary {i}: "))
    total+=salary
    if salary<=25000:
        j+=1
        print("juniour")
    elif salary>25000 and salary<=50000:
        m+=1
        print("mid")
    elif salary>50000 and salary<100000:
        s+=1
        print("seniour")
    else:
        print("Executive")
        e+=1

print("avg salary : ",total/8)
print(f"Counts : juniour {j} ,mid {m} ,seniour {s}, excutive {e}")

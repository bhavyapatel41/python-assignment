total=0
count1=0
count2=0
count3=0
count4=0
for i in range(1,6):
    marks=int(input(f"Enter {i} sub marks : "))
    total+=marks

    if marks<35:
        print("fail")
        count1+=1
    elif marks>=35 and marks<=49:
        print("pass")
        count2+=1
    elif marks>=50 and marks<=74:
        print("good")
        count3+=1
    else:
        print("excellent")
        count4+=1

if count1>count2 and count1>count3 and count1>count4:
    print(f"count 1 is highest : {count1}")
elif count2>count1 and count2>count3 and count2>count4:
    print(f"count 2 is highest : {count2}")
elif count3>count1 and count3>count2 and count3>count4:
    print(f"count 3 is highest : {count3}")
else:
    print(f"count 4 is highest : {count4}")

   

print(f"Excellent {count4} , good {count3} , pass {count2} , fail {count1}")
print("total",total)

poor = 0
avg = 0
good = 0
excellent = 0
outstanding = 0
total=0

for i in range(1,11):
    rating=float(input("Enter rating 0-10"))
    total+=rating
    if rating>=0 and rating<=3:
        print("poor")
        poor+=1
    elif rating>=3.1 and rating<=5:
        print("avg")
        avg+=1
    elif rating>=5.1 and rating<=7:
        print("Good")
        good+=1
    elif rating>=7.1 and rating<=9:
        print("Excellent")
        excellent+=1
    elif rating>=9.1 and rating<=10:
        print("outstanding")
        outstanding+=1
    else:
        print("invalid rating")



print(f"poor count {poor},avg count {avg}, good count {good}, excellent count {excellent}, outstanding count {outstanding}")
average = total / 10
print("avg : ",average)
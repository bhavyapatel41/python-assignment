count=0
for i in range(1,8):
    total=0
    print(f"Student {i}")
    for j in range(1,5):
        print(f"day {j}")
        attendence=input("Enter P/A : ").upper()
        if attendence=="P":
            count+=1
    per=count/5*100

    if per >= 90:
        status="Excellent"
    elif per >= 75:
        status="Good"
    else:
        status="Warning"



print("present count ",count)
print("percentage ",per)
print("status ",status)



pass_=0
fail_=0
highest_per=0
lowest_per=0
Topper_name=""
Lowest_name=""
for i in range(1,4):
    name=input("Enter name : ")
    total=0
    for j in range(1,4):
        marks=float(input(f"Enter marks {j}: "))
        total+=marks
        percentage=(total/3)

        if marks>=35:
            print("pass")
            pass_+=1
            if marks>=90:
                print("A")
            elif marks>=70:
                print("B")
            elif marks>=50:
                print("C")
            else:
                print("D")
        else:
            fail_+=1
            print("Fail")
    if percentage>highest_per:
        highest_per=percentage
        Topper_name=name
    if percentage < lowest_per:
        lowest_per = percentage
        Lowest_name = name
    print(total,percentage)

print(f"{Topper_name} got highest per {highest_per} ")
print(f"{Lowest_name} got highest per {Lowest_name} ")

print(f"Pass count {pass_} , fail count {fail_}")
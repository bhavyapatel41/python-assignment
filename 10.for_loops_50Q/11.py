userName=input("Enter username : ")
count_d=0
count_u=0
length=0
first_ch=0
special_ch=0
score=0
for i in userName:
    if len(userName)>=8:
        # length+=1
        score+=1
    elif userName[0]>='A' and userName[0]<='Z':
            # first_ch+=1
            score+=1
    elif i>='0' and i<='9':
        count_d+=1
        score+=1
    elif i=="_":
        count_u+=1
        score+=1
    else:
        special_ch+=1
        score+=1

if score>=4:
     print("valid")
elif score>=2:
     print("needs improvement")
else:
     print("invalid")

print(score)
print(f"digits {count_d}, underscore {count_u} , sp {special_ch}")
    
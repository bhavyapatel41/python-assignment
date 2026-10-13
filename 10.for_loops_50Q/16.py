password=input("Enter password : ")

count_u=0
count_l=0
count_d=0
count_s=0
length=len(password)

for i in password:

    if i>='A' and i<='Z':
        count_u+=1  
    elif i>='a' and i<='z':
        count_l+=1
    elif i>='0' and i<='9':
        count_d+=1
    else:
        count_s+=1

print(f"percentage of uppercase : {(count_u/length)*100}")
print(f"percentage of lowercase : {(count_l/length)*100}")
print(f"percentage of digits : {(count_d/length)*100}")
print(f"percentage of special character : {(count_s/length)*100}")


if count_u > count_l and count_u > count_d and count_u > count_s:
        print("Dominant: Uppercase")

elif count_l > count_u and count_l > count_d and count_l > count_s:
        print("Dominant: Lowercase")

elif count_d > count_u and count_d > count_l and count_d > count_s:
        print("Dominant: Digits")

elif count_s > count_u and count_s > count_l and count_s > count_d:
        print("Dominant: Special Characters")

else:
        print("Dominant: Tie")  


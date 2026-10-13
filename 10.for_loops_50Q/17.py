#highest marks logic left
highest_marks=0
topper=""
count1=0
count2=0
count3=0
count4=0
for i in range(1,3):
    name=input("Enter name : ")
    marks=float(input(f"Enter marks {i} : "))

    if marks<35:
            print("fail")
    elif marks>=35 and marks<=49:
            print("C")
    elif marks>=50 and marks<=74:
            print("B")
    else:
            print("A")

    if marks>highest_marks:
                highest_marks=marks
                topper=name

    vowel=0
    consonants=0
    for j in name:
            if j in "aeiouAEIOU":
                vowel+=1
            elif j>'A' and j<'Z' or j>'a' and j<'z':
                consonants+=1
    if vowel>consonants:
                print(f"{name} vowels win",vowel)
    elif consonants>vowel:
                print(f"{name} consonants win",consonants)
    else:
                print(f"{name} Draw")   
    

print(f"highest marks : {highest_marks},name:  {topper}")  
    
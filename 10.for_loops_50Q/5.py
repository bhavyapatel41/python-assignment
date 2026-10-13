sentence=input("Enter sentence : ")
word=sentence.split()

for i in word:
    length=len(i)
    print(f"{length} is length of {i}")

if length<=3:
        print("short")
elif length>4 and length<6:
        print("medium")
else:
        print("long")
#A1. Output Prediction --- Easy

#1
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")
#1,2,3,4 Finishes

#2
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)
#skyl

#3
n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2
#2,4,6

#A2. Write a Program --- Medium

#4
num=int(input("Enter a number : "))
for i in range(1,num+1):
    if i==7:
        break
    print(i)

#5
string="bhavya"
ch="v"
for i in string:
    if i==ch:
        break
    print(i,end=" ")
print("\n")
#6
arr=[2,3,5,-6,78,8]
for i in arr:
    if i<0:
        break
    print(i)

#A3. Think Carefully --- Challenging

#8
sentence=input("Enter sentence : ")
word=sentence.split()
target=input("Enter target word : ")
for i in word:
    
    if word==target:
        print("found")
        break
else:
    print("Not founded")




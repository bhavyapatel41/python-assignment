#Section B --- Practice Problems on continue

#9
for i in range(1, 7):
    if i == 4:
        continue
    print(i)

#1,2,3,5,6

#10
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")

#dcton

#11
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

#2,4,5

#B2. Write a Program --- Medium

#12
n=int(input("Enter n : "))

for i in range(1,n+1):
    if i%3==0:
        continue
    print(i)

#13

string="bhavya"
ch="v"
for i in string:
    if i==ch:
        continue
    print(i,end=" ")


#14
#marks=float(input("Enter marks : "))

while True:
    
    marks=float(input("Enter marks : "))
    if marks==0:
        break
    if marks<=40:
            continue
    print(marks)

#B3. Think Carefully --- Challenging

#15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)

# A 1
# B 1
# A 3
# B 3
# A 4
# B 4

#16
n = 0

while n < 5:
    n+=1
    if n == 3:
        continue
    
    print(n)

#17
word="Bhavya".lower()
consonents=0
for i in word:
    if i in "aeiou":
        continue
    consonents+=1

print(consonents)

#Section C --- Practice Problems on for-else

#18
for i in range(1, 4):
    print(i)
else:
    print("Done")
#1,2,3,done

#19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

#1,3,4,completed

#20
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")

#1,2,outside loop

#21--------------

for item in []:
    print("Inside")
else:
    print("Else block")


#C2. Write a Program --- Medium

#22

# arr1=[1,3,4]
# target=3
# for i in arr1:
#     if i==target:
#         print("Founded")
# else:
#     print("Not founded")

# #23
# string="bhavya"
# ch="v"
# for i in string:
#     if i==ch:
#         print("Funded")
#         break
# else:
#     print("not founded")

#24
# n=int(input("Enter number : "))

# for i in range(2,n):
#     if n%i==0:
#         print("non prime")    
#         break

# else:
#     print("prime")

#C3. Think Carefully --- Challenging

#25
values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")

#All are even

#27
string = input("Enter a string: ")

for i in range(0,len(string)):
    if string[i]== string[i + 1:]:
        print(string[i])
        break
else:
    print("No repeated character")

#Section D --- Practice Problems on pass

#28
for i in range(1, 4):
    if i == 2:
        pass
    print(i)

#1,2,3

#29
x = 10

if x > 5:
    pass

print("Finished")

#Finished

#30
for letter in "cat":
    pass

print("Loop ended")

#Loop ended

#D2. Write a Program --- Medium

#31
for i in range(1, 6):
    if i %2== 0:
        pass
    print(i)



#32
choice = int(input("Enter your choice: "))

if choice==1:
    print("Option 1")
elif choice==2:
    pass
else:
    print("Unknown option")

print("end")

#D3. Think Carefully --- Challenging

#33
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

#1,2,3,4----pass do nothing


for i in range(1, 5):
    if i == 3:
        continue
    print(i)

#1,2,4---3 skip

#34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#Section E --- Mixed Challenge Questions

#35
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")

#1,3----loop is break so else do not exceuted

#36

arr=[1,-2,3,4]
target=3
for i in range(len(arr)):
    if arr[i]<0:
        continue
    if arr[i]==target:
        print("target founded")
        break
else:
    print("target not found")

#37
arr=[1,-2,3,0,-1]

for i in range(len(arr)):
    if arr[i]==0:
        continue
    if arr[i]==-1:
        break
else:
    print("All values processed")

#38

for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")


#1 1
#1 3
#Inner loop completed
#2 1
#2 3
#Inner loop completed

#39

arr=[1,2,34,-4,23,24]
for i in range(len(arr)):
    if arr[i]<0:
        continue
    if arr[i]%4==0 and arr[i]%6==0:
        print("divisible by both 4 and 6 : ",arr[i])
        break
else:
    print("no number divisible by both 4 and 6")
   
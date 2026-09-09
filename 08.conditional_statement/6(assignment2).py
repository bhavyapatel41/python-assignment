#Assignment 2 
#LEVEL--1
#1
number=int(input("Enter number : "))
if number>0:
    print("positive")
elif number<0:
    print("negative")
else:
    print("zero")

#2
if number>0:
    print("positive ")
    if(number%2==0):
       print("Even")
    else:
       print("odd")
elif number<0:
    print("negative ")
    if(number%2==0):
          print("Even")
    else:
          print("odd")
else:
    print("zero")

#3

num1=int(input("Enter num 1 : "))
num2=int(input("Enter num 2 : "))

if(num1>num2):
    print(f"num {num1} is largest .")
elif num1==num2:
    print(f"equal")
else:
    print(f"num {num2} is largest .")

#4
# n1=int(input("Enter num 1 : "))
# n2=int(input("Enter num 2 : "))
# n3=int(input("Enter num 3 : "))

# if n1<n2 and n1<n3:
#     print(f"{n1} is smallest")
# elif n2<n1 and n2<n3:
#     print(f"{n2} is smallest")
# else:
#     print(f"{n3} is smallest")

#5
n1=int(input("Enter num 1 : "))
n2=int(input("Enter num 2 : "))
n3=int(input("Enter num 3 : "))

if n1>n2 and n1>n3:
    print(f"{n1} is largest")
elif n2>n1 and n2>n3:
    print(f"{n2} is largest")
else:
    print(f"{n3} is largest")

# #6
# number1=int(input("Enter num : "))

# if number1%5==0 and number1%7==0:
#     print("Divisible by both 5 and 11")
# elif number1%5==0:
#     print("Divisible only by 5")
# elif number1%7==0:
#     print("Divisible only by 7")
# else:
#     print("Divisible by neither")

#7
number1=int(input("Enter num : "))

if number1%3==0 and number1%7==0:
    print("Divisible by 3 both 11")
elif number1%3==0:
    print("Divisible only by 3")
elif number1%7==0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")

#8
marks1=int(input("Enter marks : "))

if marks1<0 or marks1>100:
    print("invalid")
elif marks1>=40:
    print("Pass")
else:
    print("Fail")

#9
marks2=int(input("Enter marks (for grade): "))

if marks2>=90 and marks2<=100:
    print("A")
elif marks2>=80 and marks2<=89:
    print("B")
elif marks2>=70 and marks2<=79:
    print("C")
elif marks2>=60 and marks2<=69:
    print("D")
elif marks2>=40 and marks2<=59:
    print("E")
else:
    print("Fail")

#10
age=int(input("Enter age : "))
if age>=18 and age<=120:
    print("Can Vote")
elif age <18:
    print("Cannot Vote")
else:
    print("invalid age")
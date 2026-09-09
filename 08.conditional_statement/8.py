#LEVEL--3

# #21
# a=int(input("Enter a : "))
# b=int(input("Enter b : "))
# c=int(input("Enter c : "))

# if a+b>c and a+c>b and b+c>a:
#     print(" valid triangle")
#     if a==b==c:
#         print(" Equilateral: all three sides equal")
#     elif a==b or b==c or c==a:
#         print("Isosceles : exactly two sides equal")
#     else:
#         print("Scalene: all sides different")
    
# else:
#     print("invalid triangle")

#22

# account_balance=float(input("Enter balance : "))
# withdrawal_amount=float(input("Enter amount : "))

# if withdrawal_amount<(account_balance+500) and withdrawal_amount%100==0 and withdrawal_amount>0:
#     print("Withdrwal successful\n")
#     print(f"Remaining balance : {account_balance-withdrawal_amount}")
# else:
#     print("invalid amount")

# if withdrawal_amount>0:
#     if withdrawal_amount<(account_balance-500):
#         if withdrawal_amount%100==0:
#             print("Withdrwal successful\n")
#             print(f"Remaining balance : {account_balance-withdrawal_amount}")
#         else:
#             print("invalid amount")
#     else:
#         print("insufficient balance to withdraw money")
# else:
#     print("amount should be grater then zero")

#23

# username=input("Enter username : ")
# password=input("Enter password : ")
# if username!="admin":
#     print("User not found")
# elif password!="python123":
#         print("Wrong password")
# else:
#         print("login succesful")    

#24

# purchase_amount=float(input("Enter purchase amount : "))
# print("Purchase: ",purchase_amount)
# discount_amount=0
# if purchase_amount<500:
#        print("Discount : 0%")
#        discount_amount=purchase_amount
# elif purchase_amount>=500 and purchase_amount<=999:
#        print("Discount : 5%")
#        discount_amount=purchase_amount*0.05
# elif purchase_amount>=1000 and purchase_amount<=1999:
#        print("Discount : 10%")
#        discount_amount=purchase_amount*0.1
# elif purchase_amount>=2000 and purchase_amount<=4999:
#        print("Discount : 15%")
#        discount_amount=purchase_amount*0.15
# else:
#        print("Discount : 20%")
#        discount_amount=purchase_amount*0.2

# print(f"discount amount: {discount_amount}")
# print(f"final amount : {purchase_amount-discount_amount}")

#25
# m1=int(input("Enter a : "))
# m2=int(input("Enter b : "))
# m3=int(input("Enter c : "))
# avg=(m1+m2+m3)/3
# if m1>=35 and m2>=35 and m3>35:
       
#     if avg>=75:
#         print("Distinction")
#     elif avg>=60 and avg<=74:
#        print("first class")
#     elif avg>=50 and avg<59:
#         print("second class")
#     else:
#         print("pass")
# else:
#      print("fail")
    
#26

# day=int(input("Enter day : "))
# month=int(input("Enter month : "))
# year=int(input("Enter year : "))

# if month>=1 and month<=12:
#     if month%2==0:


#27
# hours=int(input("Enter hours : "))
# min=int(input("Enter min : "))
# sec=int(input("Enter sec : "))

# if hours>=0 and hours<=23:
#     if min>=0 and min<=59:
#         if sec>=0 and sec<=59:
#             print("valid time")
# else:
#     print("invalid time")            

#28

# person1=input("enter name 1: ")
# age1=input("enter age 1 : ")
# person2=input("enter name 2: ")
# age2=input("enter age 2 : ")
# person3=input("enter name 3: ")
# age3=input("enter age 3 : ")

# if age1>age2 and age1>age3:
#     print(f"{person1} is youngest")
# elif age2>age1 and age2>age3:
#      print(f"{person2} is youngest")
# elif age3>age1 and age3>age2:
#      print(f"{person3} is youngest")
# elif age1==age2 or age2==age3 or age3==age2:
#      print("2 people have same age")
# else:
#      print("All three have the same age")

#29
# num1=int(input("Enter num1 : "))
# num2=int(input("Enter num2 : "))
# num3=int(input("Enter num3 : "))

#30
student_age=int(input("Enter age : "))
marks=float(input("Enter marks : "))
family_income=float(input("enter income : "))
attendence_per=float(input("enter attendece percentage : "))

if student_age>=18 and student_age<=25:
    if marks>=85:
        if attendence_per>=75:
                if family_income<=300000:
                    print("Scholarship Approved")
                else:
                    print("family income greater then 3LPA")
        else:
             print("attendence is less then 75 ")    
    else:
         print("Marks are below 85")
else:
     print("invalid age")

# if student_age<18 or student_age>25:
#     print("age invalid")
# elif marks<85:
#      print("marks is less then 85")
# elif attendence_per<75:
#      print("attendece is less then 75")
# elif family_income>300000:
#      print("family income greater then 3LPA")
# else:
#      print("scholarship Approved")
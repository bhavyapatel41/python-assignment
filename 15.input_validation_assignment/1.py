# # #Part A — Intermediate Problems

# # #1

# # marks=int(input("Enter marks : "))

# # while not (marks>0 and marks<=100):
# #     print("Invalid marks enter again...")
# #     marks=int(input("Enter marks : "))

# # print("marks accepted",marks)

# # #2
# # num=int(input("Enter num : "))

# # while num<0:
# #     print("number should be greater than 0 ")
# #     num=int(input("Enter num : "))

# # print("+ve int : ",num)

# # #3
# # age=int(input("Enter age : "))

# # while age<0 or age>120:
# #     print("error ...0<age<=120")
# #     age=int(input("Enter age : "))

# # print("age : ",age)

# # #4

# # while True:
# #     print("\n--- Menu ---")
# #     print("1. View profile")
# #     print("2. Edit profile")
# #     print("3. Settings")
# #     print("4. Exit")

# #     choice = input("Enter your choice (1-4): ")

# #     match choice:
# #         case "1":
# #             print("Viewing profile...")

# #         case "2":
# #             print("Editing profile...")

# #         case "3":
# #             print("Opening settings...")

# #         case "4":
# #             print("Exiting program...")
# #             break

# #         case _:
# #             print("Invalid choice! Please enter a number between 1 and 4.")

# #5
# # password=input("Enter password : ").strip()

# # while len(password)<8:
# #     password=input("Enter password of atleast 8 char: ").strip()

# # print("entery granted")

# # #6
# # temperature = float(input("Enter temperature between -20 and 45: "))

# # while not (-20 <= temperature <= 45):
# #     temperature = float(input("Enter temperature between -20 and 45: "))

# # print("Valid temperature entered")

# #7

# balance=5000
# amount=float(input("Enter withdrawal amount :  "))

# while True:
#     if amount<=0 or amount>balance:
#         amount=float(input("Enter withdrawal amount :  "))
#     else:
#         balance-=amount
#         break

# print("balance : ",balance)

# #8

# username=input("Enter username : ").strip()

# while True:
#     if username==" ":
#         username=input("Enter username : ").strip()
#     elif len(username)<6:
#         username=input("Enter username : ").strip()
#     elif " " in username:
#         username = input("Enter username: ").strip()
#     else:
#         print("accepted",username)
#         break

# #9
# num=int(input("Enter num : "))

# while True:
#     if num>0 and num%3==0 and num%5==0:
#         print(num)
#         break
#     else:
#         num=int(input("Enter num again : "))

#10
# pin=1234
# Enter_pin=int(input("Enter pin : "))
# for i in range(2):
    
#     if pin==Enter_pin:
#         print("access granted")
#         break
#     else:
#         Enter_pin=int(input("Enter pin : "))
# else:
#     print("you had only 3 attempt try again after 5 min")

#11
num=int(input("Enter num : "))

while not(num<=50 and num>=10):
    num=int(input("Enter num : "))

if num%2==0:
    print("even")
else:
    print("odd")

#12
balance=2000
amount=float(input("Enter deposite amount :  "))

while True:
    if amount<=0:
        amount=float(input("Enter deposite amount :  "))
    else:
        balance+=amount
        break

print("balance : ",balance)




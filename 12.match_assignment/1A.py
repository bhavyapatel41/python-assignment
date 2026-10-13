# #Q1. Food Ordering System

# choice=int(input("Enter choice for food : "))

# match choice:
#     case 1:
#         print("pizza")
#     case 2:
#         print("burger")
#     case 3:
#         print("pasta")
#     case 4:
#         print("sandwich")
#     case _:
#         print("invalid choice")

# #Q2. Mobile Settings
# choice1=input("Enter your choice : ")
# match choice1:
#     case 1:
#         print("wifi")
#     case 2:
#         print("bluetooth")
#     case 3:
#         print("mobile data")
#     case 4:
#         print("airplane mode")
#     case 5:
#         print("Exit")  
#     case _:
#         print("invalid setting")

# choice = int(input("Enter your choice:\n1. Check Balance\n2. Withdraw Money\n3. Deposit Money\n4. Change PIN\n5. Exit\n"))

# match choice:
#     case 1:
#         print("Check Balance")
#     case 2:
#         print("Withdraw Money")
#     case 3:
#         print("Deposit Money")
#     case 4:
#         print("Change PIN")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid choice")
# #4
# color=input("red,yellow,green\nEnter your choice : ").lower()

# match color:
#     case "red":
#         print("stop")
#     case "yellow":
#         print("wait")
#     case "green":
#         print("go")
#     case _:
#         print("invalid")

# #5
# choice = int(input("Enter choice: "))

# match choice:
#     case 1:
#         print("Opening Profile")
#     case 2:
#         print("Opening Courses")
#     case 3:
#         print("Opening Marks")
#     case 4:
#         print("Opening Attendance")
#     case 5:
#         print("Logging out")
#     case _:
#         print("Invalid choice")

# #6
# category = int(input("Enter category: "))

# match category:
#     case 1:
#         print("Opening Electronics")
#     case 2:
#         print("Opening Clothing")
#     case 3:
#         print("Opening Books")
#     case 4:
#         print("Opening Grocery")
#     case 5:
#         print("Exit")
#     case _:
#         print("Invalid category")

# #7
# service = int(input("Enter service: "))

# match service:
#     case 1:
#         print("Opening Account Balance")
#     case 2:
#         print("Opening Mini Statement")
#     case 3:
#         print("Opening Fund Transfer")
#     case 4:
#         print("Opening Bill Payment")
#     case 5:
#         print("Opening Customer Support")
#     case _:
#         print("Invalid service")

# #8
# show = int(input("Enter show: "))

# match show:
#     case 1:
#         print("Morning Show Selected")
#     case 2:
#         print("Afternoon Show Selected")
#     case 3:
#         print("Evening Show Selected")
#     case 4:
#         print("Night Show Selected")
#     case _:
#         print("Invalid show")

# #9
# weather = input("Enter weather: ")

# match weather:
#     case "sunny":
#         print("Wear sunglasses")
#     case "rainy":
#         print("Carry an umbrella")
#     case "cloudy":
#         print("Weather may change")
#     case "snowy":
#         print("Wear warm clothes")
#     case _:
#         print("Unknown Weather")

# #10
# payment = input("Enter payment method: ")

# match payment:
#     case "upi":
#         print("UPI Payment Selected")
#     case "card":
#         print("Card Payment Selected")
#     case "cash":
#         print("Cash Payment Selected")
#     case "wallet":
#         print("Wallet Payment Selected")
#     case _:
#         print("Invalid Payment Method")
# #11
# extension = input("Enter extension: ")

# match extension:
#     case "pdf":
#         print("Document")
#     case "jpg":
#         print("Image")
#     case "png":
#         print("Image")
#     case "mp3":
#         print("Audio File")
#     case "mp4":
#         print("Video File")
#     case _:
#         print("Unknown File Type")

# #12
# role = input("Enter role: ")

# match role:
#     case "admin":
#         print("Full Access")
#     case "teacher":
#         print("Teacher Dashboard")
#     case "student":
#         print("Student Dashboard")
#     case "guest":
#         print("Limited Access")
#     case _:
#         print("Invalid Role")

# #13
# day=input("Enter day : ")
# match day:
#     case 1 | 2 | 3 |4| 5:
#         print("weekday")
#     case 6|7:
#         print("weekend")
#     case _:
#         print("invalid ")

# #14

# priority=int(input("Enter priority number : "))
# match priority:
#     case 1|2:
#         print("Normal priority")
#     case 3|4:
#         print("urgent priority")
#     case _:
#         print("invalid")

# # #15
# # membership = int(input("Enter membership level: "))

# # match membership:
# #     case 1 | 2:
# #         print("Basic Membership")

# #     case 3 | 4:
# #         print("Premium Membership")

# #     case _:
# #         print("Invalid Membership")

# #16
# user=int(input("Enter user Type : "))
# option=int(input("Enter option : "))
# match user:
#     case 1:
#         match option:
#             case 1:
#                 print("student courses")
#             case 2:
#                 print("student marks")
#             case 3:    
#                 print("student attendence")
#     case 2:
#         match option:
#             case 1:
#                 print("teacher view courses")
#             case 2:
#                 print("teacher can enter marks")
#             case 3:    
#                 print("teacher view attendence")
        
# #17
# account=int(input("Enter user Type : "))
# show=int(input("Enter option : "))
# match account:
#     case 1:
#         match show:
#             case 1:
#                 print("saving check balance")
#             case 2:
#                 print("saving deposite")
#             case 3:    
#                 print("saving withdraw")
#     case 2:
#         match show:
#             case 1:
#                 print("current check balance")
#             case 2:
#                 print("current deposite")
#             case 3:    
#                 print("current withdraw")
#     case _:
#         print("invalid")
        
# #18

# category = int(input("Enter category: "))

# match category:
#     case 1:
#         product = int(input("Enter product: "))
#         match product:
#             case 1:
#                 print("Mobile")
#             case 2:
#                 print("Laptop")
#             case 3:
#                 print("Headphones")
#             case _:
#                 print("Invalid")

#     case 2:
#         product = int(input("Enter product: "))
#         match product:
#             case 1:
#                 print("Shirt")
#             case 2:
#                 print("Jeans")
#             case 3:
#                 print("Shoes")
#             case _:
#                 print("Invalid")

#     case _:
#         print("Invalid Category")



# #19
# category = int(input("Enter category: "))

# match category:
#     case 1:
#         food = int(input("Enter food: "))
#         match food:
#             case 1:
#                 print("Paneer Selected")
#             case 2:
#                 print("Dal Selected")
#             case 3:
#                 print("Veg Biryani Selected")
#             case _:
#                 print("Invalid Food")

#     case 2:
#         food = int(input("Enter food: "))
#         match food:
#             case 1:
#                 print("Chicken Biryani Selected")
#             case 2:
#                 print("Chicken Curry Selected")
#             case 3:
#                 print("Fish Fry Selected")
#             case _:
#                 print("Invalid Food")

#     case _:
#         print("Invalid Category")

# #20
# a=int(input("Enter a : "))
# b=int(input("Enter b : "))
# oparation=input("Menu : \n+ Addtion\n- substraction\n* multiplication\n/ division\n% modulus\n//floor-division \nEnter your choice : ")

# match oparation:
#     case "+":
#         print("Addition ",a+b)
#     case "-":
#         print("Substraction : ",a-b)
#     case "*":
#         print("multiplication : ",a*b)
#     case "/":
#         print("division : ",a/b)
#     case "%":
#         print("modulus : ",a%b)
#     case "//":
#         print("modulus : ",a//b)
#     case _:
#         print("invalid")

#21
choice1=int(input("1.F\n2.C\nEter chocie : "))

match choice1:
    case 1:
        print("Celsius to Fahrenheit")
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f)
    case 2:
        print("Fahrenheit to Celsius")
        f = float(input("Enter temperature in F: "))
        c=(f-32)*5/9
        print(c)


#22
choice2=int(input("menu : \n1 → Kilometers to Meters\n2 → Meters to Kilometers\n3 → Kilograms to Grams\n4 → Grams to Kilograms"))
value=float(input("Enter value : "))

match choice2:
    case 1:
        #value=float(input("Enter value : "))
        print("in meters : ",value*1000)
    case 2:
       print("in m",value/1000)
    case 3:
        print(value * 1000, "grams")
    case 4:
        print(value / 1000, "kilograms")
    case _:
        print("Invalid choice")
    
#23
account = int(input("Enter account type: "))

match account:
    case 1:
        print("Savings Account")
    case 2:
        print("Current Account")
    case _:
        print("Invalid Account Type")
        

amount = float(input("Enter amount: "))

if amount > 0:
    print("Withdrawal Request Accepted")
else:
    print("Invalid Amount")

#24

choice = int(input("Menu : \n1 → Start Exam\n2 → View Result\n3 → Exit\nEnter choice: "))

match choice:

    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result")

    case 3:
        print("Exit")

    case _:
        print("Invalid Choice")

#25

choice = int(input("Menu : \n1 → Regular\n2 → Premium\n3 → VIP\nEnter choice: "))

match choice:

    case 1:
        ticket = "Regular Ticket"

    case 2:
        ticket = "Premium Ticket"

    case 3:
        ticket = "VIP Ticket"

    case _:
        print("Invalid Choice")
        exit()

age = int(input("Enter age: "))

if age < 5:
    print("Free Entry")
else:
    print(ticket)

#26

device=int(input("Menu : \n1 → Light\n2 → Fan\n3 → AC\n4 → TV\nEnter device: "))

match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")

#27

department=int(input("Menu : \n1 → General Medicine\n2 → Cardiology\n3 → Orthopedics\n4 → Pediatrics\n5 → Emergency\nEnter department: "))

match department:
    case 1:
        print("General Medicine")
    case 2:
        print("Cardiology")
    case 3:
        print("Orthopedics")
    case 4:
        print("Pediatrics")
    case 5:
        print("Emergency")
    case _:
        print("Invalid Department")


#28

choice=int(input("Menu : \n1 → Book Ticket\n2 → Cancel Ticket\n3 → Check PNR\n4 → Train Schedule\n5 → Exit\nEnter choice: "))

match choice:
    case 1:
        print("Ticket Booking Selected")
    case 2:
        print("Ticket Cancellation Selected")
    case 3:
        print("PNR Status Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")

#29

choice=int(input("Menu : \n1 → Search Book\n2 → Issue Book\n3 → Return Book\n4 → View Issued Books\n5 → Exit\nEnter choice: "))
match choice:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")

#30

status=input("Enter status: ")

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order is confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Status")


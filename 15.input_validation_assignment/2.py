#Part B — Challenging Problems

#13
num=int(input("Enter num : "))

while num<0 or num>100:
    
    num=int(input("Enter num : "))

print("num : ",num)

#14
marks=int(input("Enter marks : "))

while not (marks>0 and marks<=100):
    print("Invalid marks enter again...")
    marks=int(input("Enter marks : "))

print("marks accepted",marks)
if marks>=75:
    print("Distinction")
elif marks>=35 and marks<75:
    print("pass")
else:
    print("fail")

#15

username=input("Enter username : ").strip()
password=input("Enter password : ")

while True:
    if len(username)<5:
        username=input("Enter username : ").strip()
    elif " " in username:
        username=input("Enter username : ").strip()
    if len(password)<8:
        password=input("Enter password : ")

    elif " " in password:
        password=input("Enter password : ")

    else:
        print(password,username)
        break

#16
a=int(input("Enter a : "))
b=int(input("Enter b : "))
while True:
    
    oparator=input("Enter operator (+, -, *, or /): ")
    if oparator not in "+-*/":
        oparator=input("Enter operator (+, -, *, or /): ")
    else:

        match oparator:
            case "+":
                print(a+b)
                break
            case "-":
                print(a-b)
                break
            case "*":
                print(a*b)
                break
            case "/":
                if b==0:
                    b=int(input("Enter non-zero divisor : "))
                    continue
                else:
                    print(a/b)
                    break

17

balance=10
choice=int(input("menu : \n1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit\nEnter your choice : "))

while True:
    match choice:
        case 1:
            print("balance : ",balance)
        case 2:
            amount=int(input("Enter deposite amount : "))
            if amount>0:
                balance+=amount
            else:
                print("invalid deposite amount")
                continue
        case 3:
            amount=int(input("Enter withdrawal amount : "))
            
            if amount>balance or amount<0:
                print("invalid withdrawal amount")
                continue
            else:
                balance-=amount
        case 4:
            print("exit")
            break
    choice=int(input("menu : \n1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit\nEnter your choice : "))

18
day=int(input("Enter day : "))
month=int(input("ENter month : "))
while True:
   
    if day<1 or day>31:
        day=int(input("Enter day between 1 to 31: "))
    elif month<1 or month>12:
            month=int(input("ENter month between 1 to 12 : "))
    else:
        print(f"{day}/{month}/2026")
        break

#19

qut=float(input("Enter quantity : "))
price=float(input("Enter price : "))

while True:
    if qut<0:
         qut=float(input("Enter +ve  quantity : "))
    elif price<0:
         price=float(input("Enter +ve price : "))
    else:
         print("cost : ",price*qut)
         break

#20

while True:
    n = int(input("Enter how many numbers (1-20): "))

    if n < 1 or n > 20:
        print("Enter a number between 1 and 20")
    else:
        total = 0
        for i in range(n):
            num = float(input("Enter number: "))
            total = total + num

        average = total/n

        print("Average:", average)
        
        break

#22

num=int(input("Enter num : "))

while not(num>=1 and num<=10):
    num=int(input("Enter num : "))

print(num)          

#23
sum=0

for i in range(3):
        score=float(input("Enter score : "))
        if score<0 or score>100:
            score=float(input("Enter score again: "))
        else:
            sum+=score
            
print(sum/3)

#24


balance = 10000

while True:
    amount = int(input("Enter withdrawal amount (₹): "))

    if amount <= 0:
        print("Amount must be positive.")
    elif amount > balance:
        print("Insufficient balance!")
    elif amount % 100 != 0:
        print("Enter a multiple of 100.")
    else:
        balance -= amount
        print(f"Withdrawn amount : {amount}")
        print(f"Remaining balance : {balance}")
        break

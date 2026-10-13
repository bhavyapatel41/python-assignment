balance=0
count_d=0
count_w=0
for i in range(1,3):
    trans=input("d for deposite and w for withdrwal").lower()

    if trans=="d":
        deposite=float(input("Enter deposite amount : "))
        balance+=deposite
        count_d+=1
    elif trans=="w":
        withdrawal=float(input("Enter withdrawal amount : "))
        if balance<=1000:
            print("Low balance")
        elif balance<withdrawal:
            print("balance insufficient")
        else:
            balance-=withdrawal
            count_w+=1
    else:
        print("incorrect transiction attempt")

print(f"final balance {balance} and deposite count {count_d} , withdrwal count {count_w}")




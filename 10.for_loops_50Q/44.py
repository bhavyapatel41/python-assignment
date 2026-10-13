balance=0
deposite_count=0
withdrawal_count=0
for i in range(1,11):
    transction=input("deposite/withdrawal (D/W)").upper()
    if transction=="D":
        deposite=float(input("Enter deposite amount : "))
        deposite_count+=1
        balance+=deposite
    elif transction=="W":
        
        if balance<500:
            print("low balance")
        elif balance<0:
            print("overdraft")
        else:
            withdrawal=float(input("Enter withdrawal amount : "))
            balance-=withdrawal
            withdrawal_count+=1
    else:
        print("transction input error")

print(f"total withdrawal {withdrawal_count} , total deposite {deposite_count} , balance {balance}")

    


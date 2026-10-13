revenue=0
discount=0
for i in range(1,3):
    name=input(f"Enter customer name :{i} ")
    total=0
    for j in range(1,4):
        prices=float(input(f"Enter prices {j}: "))
        total+=prices
    if total>=2000:
            discount=total*0.15
    elif total>=1000:
            discount=total*0.1
    else:
            discount=0
    
    member=input("Are u an member (y/n)").lower()
    if member=="y":
            mem_discount=total*0.05
    else:
            mem_discount=0
    total_discount = discount + mem_discount
    final_bill =total - total_discount

    revenue+=final_bill
    print(f"name : {name} , total : {total}, discount : {total_discount},final bill:{final_bill}")
    print()

print(" total revenue : ",revenue)
             
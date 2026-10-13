
budget=0
regular=0
premium=0
luxury=0
total=0

for i in range(1,3):
    price=float(input(f"Enter product {i} price :"))
    total=total+price
    if price<500:
        print("Budget")
        budget+=1
    elif price>=500 and price<2000:
        print("regular")
        regular+=1
    elif price>=2000 and price<5000:
        print("premium")
        premium+=1
    else:
        print("luxuary")
        luxury+=1

print("Total amount : ",total)
print("Avg product price : ",total/8)
print(f"budget {budget} , regular {regular}, premium {premium} ,luxury {luxury}")
    

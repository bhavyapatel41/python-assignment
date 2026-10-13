total=0
total_discount=0
discount5=0
discount2=0
discount1=0
for i in range(1,11):
    discount=0
    prices=int(input(f"Enter {i} prices : "))
    total+=prices
    if prices>=5000:
        discount=prices*0.2
        discount5+=1
    elif prices>=3000:
        discount=prices*0.15
        discount2+=1
    elif prices>=1000:
        discount=prices*0.1
        discount1+=1
    else:
        print("no discount")
        
    total_discount+=discount
    

print(f"20% count {discount5}\n15% count {discount2}\n10% count {discount1}")
print("total price",total)
print("Total discount",total_discount)
print("final price",total-total_discount)


    



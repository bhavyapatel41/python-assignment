total=0
for i in range(1,6):
    units=float(input("Enter units : "))

    if units>=100:
        bill=5*units
    elif units>=200:
        bill=100*5 +(units-100)*7
    elif units>=400:
        bill=100*5 + 100*7 + (units-200)*10
    else:
        bill=100*5 + 100*7 + 200*10 +(units-400)*15

    if bill<1000:
        print("Low")
    elif bill<=3000:
        print("medium")
    else:
        print("high")

    total+=bill
    print("total",total)
    print("bill : ",bill)


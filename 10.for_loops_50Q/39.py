collection=0
for i in range(1,9):
    age=int(input(f"Enter age {i} : "))
    distance=float(input("Enter distance to travel"))
    fare=10*distance
    if age<=5:
        passanger_fare=0
        print("free")
    elif age>=5 and age<=12:
        discount=fare*0.5
    elif age>=60:
        discount=fare*0.3
    else:
        discount=0
    passanger_fare=fare-discount
    print("Passanger fare : ",passanger_fare)
    collection+=passanger_fare



print("Total 8 passanger collection : ",collection)
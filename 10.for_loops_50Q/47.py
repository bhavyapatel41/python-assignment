count_0=0
count_1=0
count_6=0
count_20=0
h_name=""
h_qut=0



for j in range(1,9):
        name=input("Enter name : ")
        qut=int(input("Enter quantity : "))
        if qut==0:
            print("out of stock")
            count_0+=1
        elif qut>=1 and qut<=5:
            print("critical")
            count_1+=1
        elif qut>=6 and qut<=20:
            print("low")
            count_6+=1
        else:
            print("available")
            count_20+=1
        if qut>h_qut:
             h_qut=qut
             h_name=name



print(f"count : \nOut of stoock {count_0} , critical {count_1} , low {count_6} , available {count_20}")
print(f"highest qut product {h_name} : {h_qut}")



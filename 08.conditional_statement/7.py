#LEVEL--2

#11
year=int(input("enter year : "))

if year%400==0 or year%4==0 and not year%4==0:
    print("leap year")
else:
    print("not a leap year")

#12
character=input("Enter character : ")

if character>='A' and character<='Z':
    print(" Uppercase alphabet")
elif character>='a' and character<='z':
    print("lowercase")
elif character>='0' and character<='9':
    print("digit")
else:
    print("special character")

#13
character1=input("Enter character : ")

if character1 in "aeiouAEIOU":
    print("vowels")
elif character1>="0" and character1<="9":
    print("digit")
else:
    print("consonants")


#14 and 15

cost_price=float(input("Enter cost price : "))
sell_price=float(input("Enter sell price : "))

profit=sell_price-cost_price
loss=cost_price-sell_price

if cost_price<sell_price:
    print(f"profit : {(profit/cost_price)*100}")
elif cost_price>sell_price:
    print(f"loss {(loss/cost_price)*100}")
else:
    print("equal")

#16

units=int(input("Enter electricity bill units: "))

if units>=0 and units<=100:
    print(f"bill : {5*units}")
elif units>100 and units<=200:
    print(f"bill : {7*units}")
else:
    print(f"bill : {10*units}")

#17
num1=int(input("Enter num 1 : "))
num2=int(input("Enter num 2 : "))
operator=input("Enter operator : ")

if operator=="+":
    print("addition : ",num1+num2)
elif operator=="-":
    print(f"substraction : {num1-num2}")
elif operator=="/":
    if(num2==0):
        print("ZeroError")
    else:
        print(f"division : {num1/num2}")
else:
    print(f"multiplication : {num1*num2}")

#18
temp=float(input("Enter temperature : "))

if temp<0:
    print("Freezing")
elif temp>=0 and temp<=15:
    print("very cold")
elif temp>15 and temp<=25:
    print("cold")
elif temp>=26 and temp<35:
    print("normal")
else:
    print("Hot")

#19
number=int(input("Enter number : "))

if number<0:
    print("negative")
elif number>=0 and number<=50:
    print("Number is between 0 to 50")
elif number>=51 and number<=100:
    print("Number is between 51 to 100")
else:
    print("above 100")

#20
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("invalid triangle")


#Basic Level

#1
def greet():
    print("Hello, python")

greet()

#2
def show_name():
    print("bhavya")

show_name()
show_name()
show_name()

#3
def print_line():
    for i in range(20):
        print("-",end="")

print_line()
print("heading")
print_line()

#5
def show_square():
    print("****")
    print("****")
    print("****")
    print("****")

show_square()

#6
def show_menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

show_menu()
show_menu()

#7
def morning_message():
    print("Good Morning!")

def evening_message():
    print("Good Evening!")

evening_message()
morning_message()

#8
def show_student_card():
    print("Student Card")
    print("Student Name: Rahul")
    print("Roll Number: 101")

show_student_card()

#9
def print_number():
    for i in range(1,6):
        print(i)

print_number()
print_number()

#10
def show_pattern():
   for i in range(1,4):
        for j in range(i):
           print("*",end="")
        print()

show_pattern()
show_pattern()

#Intermediate Level

#11
def show_header():
    print("header")

def show_body():
    print("body")
def show_footer():
    print("footer")

show_header()
show_body()
show_footer

#12
def show_separator ():
    print("====================")

print("hello")
show_separator()
print("world !")
show_separator()

#13
def step_one():
    print("1")
def step_two():
    print("2")
def step_three():
    print("3")

step_three()
step_one()
step_two()

#14
def show_table_heading():
    print("Roll No.\tName\tMarks")


show_table_heading()

print("1\t\tBhavya\t85")
print("2\t\tKashvi\t90")

#15
def star():
    print("* * * * *")

star()
star()
star()
star()

#16
def show_welcome():
    print("welcome")
    print("CSE")

show_welcome()

#17
def show_help():
    print("Menu:\n 1.addition\n2.substraction\n3.multiplication\n4.exit")

show_help()

choice=int(input("Enter your choice : "))
a=4
b=2
while True:

    match choice:
        case 1:
            print("addition : ",a+b)
        case 2:
            print("sub : ",a-b)
        case 3:
            print("multiplication : ",a*b)
        case 4:
            break
        case _:
            print("invalid choice ")
    
#18
def open():
    print("receipt opening ...")
def close():
    print("receipt closing ...")

open()
print("receipt details..")
close()

#19
def print_box():
    print("line 1")
    print("line 2")
    print("line 3")

print_box

#20
def title():
    print("title")
def menu():
    print("menu")
def closing_message():
    print("closing message")


title()
menu()
closing_message()
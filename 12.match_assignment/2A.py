#31
choice=int(input("Enter 1 → Personal Banking \n2 → Business Banking : "))
match choice:
    case 1:
        print("Personal Banking")
        choice1=int(input("1 → Balance 2 → Transfer 3 → Loan : "))
        match choice1:
            case 1:
                print("balance")
            case 2:
                print("transfer")
            case 3:
                print("loan")

    case 2:
        print("bussiness banking")
        choice2=int(input("Enter 1 → Balance 2 → Payroll 3 → Business Loan"))
        match choice2:
            case 1:
                print("balance")
            case 2:
                print("payroll")
            case 3:
                print("business loan")
            



#32
choice = int(input("1 → Student\n2 → Teacher\n3 → Parent\nEnter role: "))

match choice:
    case 1:
        print("Student")
        choice1 = int(input("1 → Marks\n2 → Attendance\n3 → Homework\nEnter option: "))

        match choice1:
            case 1:
                print("View Student Marks")
            case 2:
                print("View Student Attendance")
            case 3:
                print("View Homework")

    case 2:
        print("Teacher")
        choice2 = int(input("1 → Enter Marks\n2 → Attendance\n3 → Assign Homework\nEnter option: "))

        match choice2:
            case 1:
                print("Enter Student Marks")
            case 2:
                print("Manage Attendance")
            case 3:
                print("Assign Homework")
            case _:
                print("Invalid option")

    case 3:
        print("Parent")
        choice3 = int(input("1 → Child Marks\n2 → Child Attendance\n3 → Contact Teacher\nEnter option: "))

        match choice3:
            case 1:
                print("View Child Marks")
            case 2:
                print("View Child Attendance")
            case 3:
                print("Contact Teacher")
            case _:
                print("Invalid option")



#33

choice = int(input("1 → Flight\n2 → Train\n3 → Bus\nEnter transport: "))

match choice:
    case 1:
        print("Flight")
        choice1 = int(input("1 → Economy\n2 → Business\nEnter class: "))

        match choice1:
            case 1:
                print("Economy Class Selected")
            case 2:
                print("Business Class Selected")
            case _:
                print("Invalid option")

    case 2:
        print("Train")
        choice2 = int(input("1 → Sleeper\n2 → AC\nEnter class: "))

        match choice2:
            case 1:
                print("Sleeper Class Selected")
            case 2:
                print("AC Class Selected")
            case _:
                print("Invalid option")

    case 3:
        print("Bus")
        choice3 = int(input("1 → Ordinary\n2 → Volvo\nEnter bus type: "))

        match choice3:
            case 1:
                print("Ordinary Bus Selected")
            case 2:
                print("Volvo Bus Selected")
            case _:
                print("Invalid option")

    case _:
        print("Invalid transport")

#34
choice = int(input("1 → Start Game\n2 → Load Game\n3 → Settings\n4 → Exit\nEnter choice: "))

match choice:

    case 1:
    
        print("Starting Game")
    case 2:
        print("Loading Game")

    case 3:
        print("Settings")
        choice1 = int(input("1 → Sound\n2 → Graphics\n3 → Controls\nEnter option: "))
        match choice1:
            case 1:
                print("Sound Settings")
            case 2:
                print("Graphics Settings")
            case 3:
                print("Controls Settings")

    case 4:
        print("Exiting Game")

    case _:
        print("Invalid choice")

#35

choice = int(input("1 → Starters\n2 → Main Course\n3 → Desserts\n4 → Drinks\nEnter category: "))

match choice:
    case 1:
        print("Starters")
        choice1 = int(input("1 → Soup\n2 → Spring Roll\n3 → Garlic Bread\nEnter item: "))

        match choice1:
            case 1:
                print("Soup Ordered")
            case 2:
                print("Spring Roll Ordered")
            case 3:
                print("Garlic Bread Ordered")
            case _:
                print("Invalid item")

    case 2:
        print("Main Course")
        choice2 = int(input("1 → Pizza\n2 → Pasta\n3 → Biryani\nEnter item: "))

        match choice2:
            case 1:
                print("Pizza Ordered")
            case 2:
                print("Pasta Ordered")
            case 3:
                print("Biryani Ordered")
            case _:
                print("Invalid item")

    case 3:
        print("Desserts")
        choice3 = int(input("1 → Ice Cream\n2 → Cake\n3 → Gulab Jamun\nEnter item: "))

        match choice3:
            case 1:
                print("Ice Cream Ordered")
            case 2:
                print("Cake Ordered")
            case 3:
                print("Gulab Jamun Ordered")
            case _:
                print("Invalid item")

    case 4:
        print("Drinks")
        choice4 = int(input("1 → Coffee\n2 → Tea\n3 → Juice\nEnter item: "))

        match choice4:
            case 1:
                print("Coffee Ordered")
            case 2:
                print("Tea Ordered")
            case 3:
                print("Juice Ordered")
            case _:
                print("Invalid item")

    case _:
        print("Invalid category")

#36
choice = int(input("1 → UPI\n2 → Card\n3 → Wallet\nEnter payment type: "))

match choice:
    case 1:
        print("UPI Payment")
        choice1 = int(input("1 → Scan QR\n2 → Enter UPI ID\nEnter option: "))

        match choice1:
            case 1:
                print("Scan QR Code")
            case 2:
                print("Enter UPI ID")
            case _:
                print("Invalid option")

    case 2:
        print("Card Payment")
        choice2 = int(input("1 → Credit Card\n2 → Debit Card\nEnter option: "))

        match choice2:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid option")

    case 3:
        print("Wallet Payment")
        choice3 = int(input("1 → Add Money\n2 → Pay Using Wallet\nEnter option: "))

        match choice3:
            case 1:
                print("Add Money to Wallet")
            case 2:
                print("Pay Using Wallet")
            case _:
                print("Invalid option")

    case _:
        print("Invalid payment type")

#37
choice = int(input("1 → Programming\n2 → Mathematics\n3 → Communication\nEnter subject: "))

match choice:
    case 1:
        print("Programming")
        choice1 = int(input("1 → Python\n2 → Java\n3 → C++\nEnter course: "))

        match choice1:
            case 1:
                print("Python Course Selected")
            case 2:
                print("Java Course Selected")
            case 3:
                print("C++ Course Selected")
            case _:
                print("Invalid course")

    case 2:
        print("Mathematics")
        choice2 = int(input("1 → Algebra\n2 → Calculus\n3 → Statistics\nEnter course: "))

        match choice2:
            case 1:
                print("Algebra Course Selected")
            case 2:
                print("Calculus Course Selected")
            case 3:
                print("Statistics Course Selected")
            case _:
                print("Invalid course")

    case 3:
        print("Communication")
        choice3 = int(input("1 → English\n2 → Presentation\n3 → Interview Skills\nEnter course: "))

        match choice3:
            case 1:
                print("English Course Selected")
            case 2:
                print("Presentation Course Selected")
            case 3:
                print("Interview Skills Course Selected")
            case _:
                print("Invalid course")

    case _:
        print("Invalid subject")

#38
choice = int(input("1 → Engine\n2 → Lights\n3 → Music\n4 → Navigation\nEnter choice: "))

match choice:
    case 1:
        print("Engine")
        choice1 = int(input("1 → Start\n2 → Stop\nEnter option: "))

        match choice1:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid option")

    case 2:
        print("Lights")
        choice2 = int(input("1 → Headlights\n2 → Indicators\n3 → Hazard Lights\nEnter option: "))

        match choice2:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid option")

    case 3:
        print("Music")
        choice3 = int(input("1 → Play\n2 → Pause\n3 → Next\n4 → Previous\nEnter option: "))

        match choice3:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Playing Next Song")
            case 4:
                print("Playing Previous Song")
            case _:
                print("Invalid option")

    case 4:
        print("Navigation")
        choice4 = int(input("1 → Start Navigation\n2 → Stop Navigation\nEnter option: "))

        match choice4:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid option")

    case _:
        print("Invalid choice")
#39
choice=int(input("1 → Employee\n2 → Manager Enter : "))
match choice:
    case 1:
        print("Employee")
        choice1=int(input("1 → View Profile\n2 → Apply Leave\n3 → View Salary : "))

        match choice1:
            case 1:
                print("view profile")
            case 2:
                print("apply leave")
                leave=int(input("Enter number of leave : "))
                if leave>0:
                    print("Leave Request Submitted")
                else:
                    print("invalid leave request")
            case 3:
                print("view salary")
    case 2:
        print("manager")
        choice2=int(input("1 → View Team\n2 → Approve Leave\n3 → View Reports\nEnter choice: "))
        match choice2:
            case 1:
                print("view team")
            case 2:
                print("approve leave")
            case 3:
                print("view reports")

#40
                   

choice = int(input("1 → Student\n2 → Teacher\n3 → Administration\nEnter role: "))

match choice:
    case 1:
        print("Student")
        choice1 = int(input("1 → Profile\n2 → Marks\n3 → Attendance\n4 → Courses\nEnter option: "))

        match choice1:
            case 1:
                print("View Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("View Student Attendance")
            case 4:
                print("View Student Courses")
    case 2:
        print("Teacher")
        choice2 = int(input("1 → Students\n2 → Enter Marks\n3 → Attendance\n4 → Courses\nEnter option: "))

        match choice2:
            case 1:
                print("View Students")
            case 2:
                print("Enter Student Marks")
            case 3:
                print("Manage Attendance")
            case 4:
                print("View Teacher Courses")
    case 3:
        print("Administration")
        choice3 = int(input("1 → Fees\n2 → Admissions\n3 → Notices\n4 → Departments\nEnter option: "))

        match choice3:
            case 1:
                print("Manage Fees")
            case 2:
                print("Manage Admissions")
            case 3:
                print("View Notices")
            case 4:
                print("View Departments")


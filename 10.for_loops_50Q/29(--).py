
# for i in range(1,6):
#     email=input("Enter email : ")
#     for j in email:
#         if j==" ":
#             print("invalid")

for i in range(5):
    string = input("Enter a string: ")
    if string.count("@") == 1:
        at_index = string.find("@")
        if "." not in string[at_index, len(string)] or " " in string or string[0, at_index] == "" or string[at_index, len(string)] == "":
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
        print("You have to enter 1 @")



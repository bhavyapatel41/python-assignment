text = "Python"
print(text[20])
#TypeError: unsupported operand type(s) for -: 'str' and 'str'
text = "Python"
text[0] = "J"
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
age = 20
print("Age: " + age)
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
text = "Python"
print(text.index("Java"))
#IndexError: string index out of range
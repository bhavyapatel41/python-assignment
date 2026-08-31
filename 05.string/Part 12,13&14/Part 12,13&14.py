# --- Task 29: Whitespace ---
messy_text = "   Python Programming   "
print("strip():", f"'{messy_text.strip()}'")
print("lstrip():", f"'{messy_text.lstrip()}'")
print("rstrip():", f"'{messy_text.rstrip()}'")

# --- Task 30: User Input ---
# Uncomment to test:
# raw_name = input("Enter your name: ")
# print("Cleaned name:", raw_name.strip())

# --- Task 31 & 32: Split ---
easy_text = "Python is easy to learn"
print("Split list:", easy_text.split())

csv_fruits = "apple,banana,mango,orange"
print("Split by comma:", csv_fruits.split(","))

# --- Task 33 & 34: Join ---
words_list = ["Python", "is", "easy"]
print("Joined with space:", " ".join(words_list))
print("Joined with dash:", "-".join(words_list))
print("Joined with slash:", "/".join(words_list))

# --- Task 35 & 36: String Formatting ---
f_name = "Alex"
f_age = 28
f_city = "Berlin"
print(f"{f_name} is {f_age} years old and lives in {f_city}.")

a = 10
b = 20
print(f"The sum is {a + b}")
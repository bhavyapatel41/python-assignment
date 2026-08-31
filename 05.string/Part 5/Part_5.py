 # --- Task 7: Basic Slicing ---
course = "Python Programming"
print(course[0:6])         # "Python"
print(course[7:18])        # "Programming"
print(course[:])           # "Python Programming"
print(course[:5])          # First 5 characters
print(course[-5:])         # Last 5 characters

# --- Task 8: Slicing with Step ---
alphabet = "ABCDEFGHIJKL"
print("Every second:", alphabet[::2])
print("Every third:", alphabet[::3])
print("Index 1 to 8, step 2:", alphabet[1:9:2])
print("Reversed:", alphabet[::-1])

# --- Task 9: Slicing with Negative Indexes ---
print("Last 5:", course[-5:])
print("Last 10:", course[-10:])
print("From end, negative step:", course[::-2])

# --- Task 10: Slicing Challenge ---
challenge_str = "DataScience"
print("First 3:", challenge_str[:3])
print("Last 3:", challenge_str[-3:])
print("Every second:", challenge_str[::2])
print("Reversed:", challenge_str[::-1])
print("Without first/last:", challenge_str[1:-1])
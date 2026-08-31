# --- Task 38: Name Processor ---
input_name = input("Enter your full name: ").strip()
print("Original input:", input_name)
print("Cleaned name:", input_name.strip())
print("Uppercase:", input_name.upper())
print("Lowercase:", input_name.lower())
print("Title case:", input_name.title())
print("Length:", len(input_name))
print("First character:", input_name[0] if input_name else "")
print("Last character:", input_name[-1] if input_name else "")
search_char = "a"
print(f"Contains '{search_char}':", search_char in input_name.lower())




# --- Task 40: Student Information ---
f_name_input = input("First name: ").strip()
l_name_input = input("Last name: ").strip()
city_input = input("City: ").strip()
course_input = input("Course: ").strip()
age_input = input("Age: ").strip()
 
full_student_name = f_name_input + " " + l_name_input
print("Title case:", full_student_name.title())
print("Uppercase:", full_student_name.upper())
print("Lowercase:", full_student_name.lower())
print("Length:", len(full_student_name))
print("First char:", full_student_name[0])
print("Last char:", full_student_name[-1])
print(f"City: {city_input}, Course: {course_input}")
print(f"The student is {age_input} years old.")
print("Course contains 'Python':", "Python" in course_input)
print("Modified course:", course_input.replace("Basic", "Advanced")) # Assuming 'Basic' is a word they might use
print("Course word count:", len(course_input.split()))
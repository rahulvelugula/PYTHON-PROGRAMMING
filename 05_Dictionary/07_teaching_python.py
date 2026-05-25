"""
Question:
You are managing students enrolled
in Basic and Advanced Python courses.

Perform the following operations:

1. Create an empty dictionary called students.

2. Add students to:
   - Basic course
   - Advanced course

3. Add new students using different methods:
   - append()
   - +=
   - extend()
   - insert()

4. Move one student from Basic
   to Advanced course.

5. Print dictionary items:
   - using .items()
   - using dictionary keys

6. Print:
   - only course names
   - only student lists
   
"""

#1
students = {}

#2
students["Basic"] = ["Alice", "Bob"]
students["Advanced"] = ["Charlie", "David", "Eve"]
print("Initial dictionary:")
print(students)

#3
students["Basic"].append("Frank")
students["Basic"] += ["Grace"]
students["Basic"].extend(["Helen"])
students["Advanced"].insert(3, "Ivy")
print("\nAfter adding new students:")
print(students)

#4
students["Basic"].remove("Bob")
students["Advanced"].append("Bob")
print("\nAfter moving 'Bob' from Basic to Advanced:")
print(students)

#5
print("\n--- Printing items (method 1: using .items()) ---")
for course, names in students.items():
    print(f"Course: {course} -> Students: {names}")

#5
print("\n--- Printing items (method 2: using keys) ---")
for course in students:
    print(f"Course: {course} -> Students: {students[course]}")

#6
print("\n--- Course names ---")
for course in students.keys():
    print(course)

#6
print("\n--- Student lists ---")
for names in students.values():
    print(names)

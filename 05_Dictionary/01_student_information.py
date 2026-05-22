"""
Question:
You are working in a school registrar's office
and need to manage student information
stored in a Python dictionary.

Perform the following operations:

1. Print all keys with their values.
2. Print all keys only.
3. Print all values only.
4. Update the course from "Literature"
   to "Foreign Languages".
5. Add:
   - Address using direct assignment
   - Phone number using update()
6. Remove "Sex" and "Hobby"
   from the dictionary.
"""

student = {
    "Firstname": "Rahul",
    "Lastname": "Sharma",
    "Sex": "Male",
    "Age": 21,
    "Course": "Literature",
    "Hobby": "Swimming"
}
#1
print("a. Keys and Values:")
for key, value in student.items():
    print(key, ":", value)
  
#2
print("\nb. Keys:")
print(student.keys())

#3
print("\nc. Values:")
print(student.values())

#4
student["Course"] = "Foreign Languages"
print("\nd. After updating course:")
print(student)

#5
student["Address"] = "New York"
student.update({"Phone number": "9876543210"})
print("\ne. After adding Address and Phone number:")
print(student)

#6
del student["Sex"]
del student["Hobby"]
print("\nf. After removing Sex and Hobby:")
print(student)

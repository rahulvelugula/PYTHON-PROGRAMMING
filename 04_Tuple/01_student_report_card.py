"""
Question:
Calculate the average marks of each student
and find the topper using tuples.

"""

n = int(input())
students = {}

for i in range(n):

    name, subject, marks = input().split()
    marks = int(marks)
    record = (subject, marks)

    if name not in students:
        students[name] = []

    students[name].append(record)

topper_name = ""
topper_average = 0

#Calculate averages
for name in sorted(students):
    total = 0
    count = 0
  
    for subject, marks in students[name]:
        total += marks
        count += 1

    average = total / count

    print(f"{name}: {average}")

    # Check topper
    if average > topper_average:
        topper_average = average
        topper_name = name

print(f"Topper: {topper_name} with average {topper_average}")

"""
Question:
You are given student enrollments
for three college courses.

Perform the following operations:

1. Find students enrolled in
   all three courses

2. Find students enrolled in
   exactly two courses.

3. Find students enrolled in
   only one course.

4. Display all the results
"""

course_a = set(input().split())
course_b = set(input().split())
course_c = set(input().split())


all_three = course_a & course_b & course_c


exactly_two = (
    (course_a & course_b)
    | (course_b & course_c)
    | (course_a & course_c)
) - all_three

only_one = (
    (course_a - course_b - course_c)
    | (course_b - course_a - course_c)
    | (course_c - course_a - course_b)
)

print(f"Students in all three courses: {all_three}")
print(f"Students in exactly two courses: {exactly_two}")
print(f"Students in only one course: {only_one}")

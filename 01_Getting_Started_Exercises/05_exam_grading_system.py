"""
Question:
A certain Computer Science professor gives 100-point exams
that are graded on the following scale:

Score Range    Grade
90 - 100       A
80 - 89        B
70 - 79        C
60 - 69        D
Below 60       F

Write a program that accepts an exam score
and prints the corresponding letter grade.
"""

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

"""
Question:
Define a function grade(score)
that returns the corresponding
letter grade based on:

90–100 : A
80–89  : B
70–79  : C
60–69  : D
Below 60 : F

If the score is outside
the range 0–100,
return "Invalid score".

Input:
A numeric score.

Output:
The corresponding letter grade.
"""

def grade(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = float(input())

result = grade(score)

if result == "Invalid score":
    print(result)

else:
    print(f"Grade: {result}")

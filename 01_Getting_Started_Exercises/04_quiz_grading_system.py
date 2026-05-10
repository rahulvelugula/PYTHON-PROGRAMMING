"""
Question:
Read a quiz score between 0 and 5
and print the corresponding grade.
Score Grade 
5       A 
4       B
3       C 
2       D
1       F
0       F
 
"""

score = int(input())

if score == 5:
    print("A")
elif score == 4:
    print("B")
elif score == 3:
    print("C")
elif score == 2:
    print("D")
else:
    print("F")

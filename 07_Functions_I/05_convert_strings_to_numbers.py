"""
Question:
Define a function toNumbers(strList)
that converts a list of numeric
strings into numeric values.

Input:
Space-separated numeric strings.

Output:
A list containing numeric values.
"""

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


strList = input().split()
toNumbers(strList)
print(strList)

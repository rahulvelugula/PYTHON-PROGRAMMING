"""
Question:
The numeric value of a name is calculated by assigning:
a = 1, b = 2, c = 3, ... z = 26

Example:
Rohith = 18 + 15 + 8 + 9 + 20 + 8 = 78

Write a program that reads a name
and prints its numerology value.
"""
name=input()
total=0
for temp in name:
    total=total+(ord(temp.lower())-ord('a')+1)
print(total)

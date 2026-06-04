"""
Question:
Define two functions:

1. sumN(n)
   - Returns the sum of the first
     n natural numbers.

2. sumNCubes(n)
   - Returns the sum of the cubes
     of the first n natural numbers.

Input:
A positive integer n.

Output:
- Sum of the first n natural numbers.
- Sum of the cubes of the first n
  natural numbers.
"""

def sumN(n):
    total = 0
    for i in range(1, n + 1):
        total += i

    return total


def sumNCubes(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3

    return total

n = int(input())

print(f"Sum of first {n} natural numbers: {sumN(n)}")
print(f"Sum of cubes of first {n} natural numbers: {sumNCubes(n)}")

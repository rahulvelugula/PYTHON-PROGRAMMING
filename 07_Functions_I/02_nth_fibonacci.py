"""
Question:
Define a function fibonacci(n)
to compute the nth Fibonacci number.

The Fibonacci sequence is:
0, 1, 1, 2, 3, 5, 8, 13, ...

Input:
A non-negative integer n.

Output:
The nth Fibonacci number.
"""

def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b

n = int(input())

print(fibonacci(n))

"""
Question:
Count the number of steps required
to reduce a number to zero.

If the number is even, divide by 2.
If the number is odd, subtract 1.

"""
#Read number
num = int(input())

steps = 0

# Reduce number to zero
while num > 0:

    # If even
    if num % 2 == 0:
        num = num // 2

    # If odd
    else:
        num -= 1

    steps += 1

print(steps)

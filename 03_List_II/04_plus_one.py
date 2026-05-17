"""
Question:
Increment a large integer represented
as a list of digits by one.

"""

#Read digits as list
digits = list(map(int, input().split()))

#Traverse from the last digit
for i in range(len(digits) - 1, -1, -1):

    # If digit is less than 9, add one and stop
    if digits[i] < 9:
        digits[i] += 1
        print(digits)
        break

    # If digit is 9, make it 0
    else:
        digits[i] = 0

# If all digits were 9
else:
    digits.insert(0, 1)
    print(digits)

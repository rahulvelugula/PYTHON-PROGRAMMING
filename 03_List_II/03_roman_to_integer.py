"""
Question:
Convert a Roman numeral into an integer.

"""

# Roman numeral values
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Read Roman numeral
s = input()

total = 0

#Traverse the string
for i in range(len(s)):

    # If current value is smaller than next value,
    #subtract it
    if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
        total -= roman[s[i]]

    # Otherwise add it
    else:
        total += roman[s[i]]

print(total)

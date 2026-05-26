"""
Question:
You are given a dictionary containing
a list of numbers.

Perform the following operations:

1. Add a new key:
   - "even"
   containing True for even numbers
   and False for odd numbers.

2. Subtract 1 from each number
   in the "numbers" list.

3. Shift the boolean list one position
   to the right in a circular manner
   to match the updated numbers.
   
"""

dictionary = {
    "numbers": [2, 3, 4, 5, 6, 7, 8, 9, 10]
}

#1
dictionary["even"] = []
for num in dictionary["numbers"]:
    dictionary["even"].append(num % 2 == 0)
print("Step 1 - Added even list:")
print(dictionary)

#2
for i in range(len(dictionary["numbers"])):
    dictionary["numbers"][i] -= 1
print("\nStep 2 - Subtracted 1 from numbers:")
print(dictionary)

#3
dictionary["even"] = (
    [dictionary["even"][-1]]
    + dictionary["even"][:-1]
)
print("\nStep 3 - Shifted boolean list to match new numbers:")
print(dictionary)

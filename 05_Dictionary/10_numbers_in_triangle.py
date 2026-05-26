"""
Question:
Create a number triangle game using
a dictionary.

Perform the following operations:

1. Ask the user to enter an integer n.

2. Create a dictionary where:
   - key = number
   - value = list containing the number
     repeated as many times as its value

3. Print the triangle pattern.

4. Ask the user if they want
   to play again.
"""

while True:
    n = int(input("Enter an integer: "))
    triangle = {}
    for i in range(1, n + 1):
        triangle[i] = [i] * i

    for key, value in triangle.items():
        print(key, value)

    choice = input(
        "Do you want to play again? (y/n): "
    ).lower()
    if choice != "y":
        break

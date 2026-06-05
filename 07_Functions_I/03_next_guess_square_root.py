"""
Question:
In Newton's Method, the next
improved guess for the square root
of x is calculated using:

nextGuess = (guess + x/guess) / 2

Define a function nextGuess(guess, x)
that returns the next improved guess.

Input:
- A floating-point number guess
- A floating-point number x

Output:
Print the next improved guess
rounded to two decimal places.

"""

def nextGuess(guess, x):
    return (guess + x / guess) / 2


guess = float(input())
x = float(input())

print(f"Next guess: {nextGuess(guess, x):.2f}")

"""
Question:
Write a Python program to count
the number of vowels in a word.

Perform the following operations:

1. Create a set containing vowels:
   a, e, i, o, u

2. Ask the user to enter a word.

3. Convert the word to lowercase.

4. Check each character to see
   if it is a vowel.

5. Count total vowels and displayy
   the result.
"""

vowels = {"a", "e", "i", "o", "u"}
word = input()
lower_word = word.lower()
count = 0

for char in lower_word:
    if char in vowels:
        count += 1
      
print(f"The word '{word}' contains {count} vowel(s).")

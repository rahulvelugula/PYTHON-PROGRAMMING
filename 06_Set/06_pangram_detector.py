"""
Question:
Write a Python program to check
whether a sentence is a pangram.

Perform the following operations:

1. Accept a sentence from the user.

2. Ignore case and non-alphabetic
   characters.

3. Create a set containing all
   letters from a to z.

4. Compare the letters in the
   sentence with the alphabet set.

5. Print whether the sentence
   is a panagram or not
"""

sentence = input()
alphabet = set("abcdefghijklmnopqrstuvwxyz")
letters = set()
for char in sentence.lower():
    if char.isalpha():
        letters.add(char)

if letters == alphabet:
    print("The sentence is a pangram.")

else:
    print("The sentence is not a pangram.")

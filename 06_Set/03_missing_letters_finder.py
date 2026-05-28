"""
Question:
Write a Python program to find
letters of the alphabet that are
missing from two given words.

Perform the following operations:

1. Ask the user to enter two words.

2. Convert both words to lowercase.

3. Create a set containing all
   letters from a to z.

4. Find letters present in the words
   using set union.

5. Find missing letters using
   set difference.

6. Display missing letters
   in alphabetical order.
   
"""

word1 = input()
word2 = input()
word1 = word1.lower()
word2 = word2.lower()

#alphabet set
alphabet = set("abcdefghijklmnopqrstuvwxyz")

present_letters = set(word1) | set(word2)

missing_letters = sorted(
    alphabet - present_letters
)

print(
    f"Letters not present in either "
    f"'{word1.capitalize()}' or "
    f"'{word2.capitalize()}' are: "
    f"{missing_letters}"
)

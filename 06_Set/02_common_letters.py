"""
Question:
Write a Python program to find
common letters between two words.

Perform the following operations:

1. Ask the user to enter two words.

2. Convert both words to lowercase.

3. Use sets to find common letters.

4. Display the common letters
   in alphabetical order.

5. If there are no common letters,
   display an appropriate message
   
"""

word1 = input()
word2 = input()
word1 = word1.lower()
word2 = word2.lower()

common = set(word1) & set(word2)

if common:
    print(
        f"The common letters between "
        f"'{word1.capitalize()}' and "
        f"'{word2.capitalize()}' are: "
        f"{set(sorted(common))}"
    )

else:
    print("No common letters found.")

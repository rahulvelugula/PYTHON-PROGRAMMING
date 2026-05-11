"""
Question:
Calculate the average word length in a sentence.

A word is defined as a sequence of
characters separated by spaces.

Ignore spaces while counting characters.
"""

sentence = input()

words = sentence.split()

total_characters = 0

for word in words:
    total_characters += len(word)

average = total_characters / len(words)

print(f"{average:.2f}")

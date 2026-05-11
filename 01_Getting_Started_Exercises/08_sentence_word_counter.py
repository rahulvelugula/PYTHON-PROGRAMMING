"""
Question:
Write a program that counts
the number of words in a sentence.

A word is defined as a sequence of
characters separated by spaces.
"""

sentence = input()

words = sentence.split()

print(len(words))

"""
Question:
An acronym is formed by taking the first letter
of each word in a phrase and converting it to uppercase.

Example:
RAM -> Random Access Memory

Write a program that reads a phrase
and prints its acronym in uppercase.
"""

phrase = input()

words = phrase.split()

acronym = ""

for word in words:
    acronym += word[0].upper()

print(acronym)

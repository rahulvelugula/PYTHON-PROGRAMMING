"""
Question:
Perform various operations on a word search puzzle list
using lists, loops, slicing, and conditions.

"""

words = [
    "cards", "park", "pets", "football", "golf",
    "crosswords", "toys", "exercise", "hobbies",
    "riding", "biking", "games", "reading",
    "movies", "walking", "concerts"
]

# a
title = f"Word search with {len(words)} words"
print(title)

# b
five_letter_words = []

for word in words:
    if len(word) == 5:
        five_letter_words.append(word)

print("\nWords with 5 letters:", five_letter_words)
print("Number of 5-letter words:", len(five_letter_words))

# c
print("\nWords with less than 5 letters:")

for index, word in enumerate(words):
    if len(word) < 5:
        print(f"- '{word}' (position {index}) has {len(word)} characters.")

# d
print("\nWords with more than 8 characters:")

for index, word in enumerate(words):
    if len(word) > 8:
        print(f"- '{word}' (position {index}) has {len(word)} characters.")

# e
print("\nWords in the second half (different from 7 characters):")

second_half = words[len(words)//2:]

for index, word in enumerate(second_half, start=len(words)//2):
    if len(word) != 7:
        print(f"- '{word}' (position {index}) → {len(word)} characters")

# f
print("\n4-letter words in the first fourth of the list:")

first_fourth = words[:len(words)//4]

for index, word in enumerate(first_fourth):
    if len(word) == 4:
        print(f"- '{word}' (position {index})")

"""
Question:
Perform operations on the seasons list
using indexing, slicing, and conditions.
"""

seasons = ["spring", "summer", "fall", "winter"]

at_least_five = []
four_or_less = []

for season in seasons:
    if len(season) >= 5:
        at_least_five.append(season)
    else:
        four_or_less.append(season)

less_than_two = seasons[:2]

at_least_two = seasons[2:]

print("Seasons with at least 5 characters:", at_least_five)

print("Seasons with 4 or fewer characters:", four_or_less)

print("Seasons with position less than 2:", less_than_two)

print("Seasons with position at least 2:", at_least_two)

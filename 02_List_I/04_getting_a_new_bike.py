"""
Question:
Maintain a list of bike features.

Find the position of the color 'blue',
remove it,
and replace it with a new color.
"""

bike_features = input().split(", ")

new_color = input()

position = bike_features.index("blue")

bike_features.remove("blue")

bike_features.insert(position, new_color)

print("Position of 'blue' in the list:", position)
print("Updated bike features:", bike_features)

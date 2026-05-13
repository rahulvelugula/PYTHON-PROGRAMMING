"""
Question:
Maintain a list of T-shirt features.

Find the position of 'add your text here',
remove it,
and replace it with new custom text.
"""

tshirt_features = input().split(", ")

new_text = input()

position = tshirt_features.index("add your text here")

tshirt_features.remove("add your text here")

tshirt_features.insert(position, new_text)

print("Position of 'add your text here' in the list:", position)
print("Updated T-shirt features:", tshirt_features)

"""
Question:
Maintain a list of paintings in an art gallery.

Check whether the painting requested by the customer
is available in the gallery or not.

"""

paintings = [
    "Starry Night",
    "The Mona Lisa",
    "The Last Supper",
    "The Scream",
    "Girl with a Pearl Earring"
]

painting = input()

if painting in paintings:
    print(f'Yes, we have "{painting}" available for purchase!')
else:
    print(f'Sorry, we dont have "{painting}" right now.')

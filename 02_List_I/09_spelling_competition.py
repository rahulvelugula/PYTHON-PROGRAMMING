"""
Question:
Categorize MSK system words into
short, intermediate, and long words.

"""

msk_words = [
    "ankle", "patella", "rib", "femur",
    "sternocleidomastoid", "tendon", "sternum",
    "abdominal external oblique", "muscle",
    "scapula", "radius", "bone", "vertebra",
    "ligament", "ulna", "skull", "clavicle"
]

short = ["leg"]
intermediate = ["cartilage"]
long = ["pectoralis major"]

#a
print("Total number of words to learn:", len(msk_words))

#b
print("\nLength of each word:")

for word in msk_words:
    print(f"{word}: {len(word)}")

#c d e
for word in msk_words:

    if len(word) <= 6:
        short.append(word)

    elif 7 <= len(word) <= 9:
        intermediate.append(word)

    else:
        long.append(word)

print("\nShort words (6 or fewer characters):", short)
print("Number of short words:", len(short))

print("\nIntermediate words (7–9 characters):", intermediate)
print("Number of intermediate words:", len(intermediate))

print("\nLong words (10+ characters):", long)
print("Number of long words:", len(long))

"""
Question:
Perform various modifications on the alan_turing list
using:
1. List slicing
2. List methods
"""

# Using list slicing

alan_turing_slice = [
    "Turing",
    "created",
    "an electromechanical machine",
    "to crack",
    "the Nazi Navy's",
    "Enigma Code"
]

alan_turing_slice[4:5] = ["shortened the war"]

alan_turing_slice[5:5] = ["by two years"]

alan_turing_slice[2:3] = ["his contribution"]

alan_turing_slice.append("saving millions of lives")

alan_turing_slice[1:2] = ["that"]

alan_turing_slice[3:4] = []

alan_turing_slice[0:1] = ["It is estimated"]

alan_turing_slice[5:6] = []

print("After performing operations using list slicing:")
print(alan_turing_slice)

# Using list methods

alan_turing_methods = [
    "Turing",
    "created",
    "an electromechanical machine",
    "to crack",
    "the Nazi Navy's",
    "Enigma Code"
]

alan_turing_methods[4] = "shortened the war"

alan_turing_methods.insert(5, "by two years")

alan_turing_methods[2] = "his contribution"

alan_turing_methods.append("saving millions of lives")

alan_turing_methods[1] = "that"

alan_turing_methods.remove("to crack")

alan_turing_methods[0] = "It is estimated"

alan_turing_methods.pop(5)

print("After performing operations using list methods:")
print(alan_turing_methods)

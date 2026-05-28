"""
Question:
Write a Python program to analyze
travel history using sets.

Perform the following operations:

1. Input cities visited by Person A.

2. Input cities visited by Person B.

3. Find:
   - Common cities
   - Cities only Person A visited
   - Cities only Person B visited
   - All cities visited

4. Display all results.

"""
person_a = set(input().split(", "))
person_b = set(input().split(", "))

common = person_a & person_b

only_a = person_a - person_b
only_b = person_b - person_a

all_cities = person_a | person_b

print(f"Cities visited by both: {common}")
print(f"Cities unique to Person A: {only_a}")
print(f"Cities unique to Person B: {only_b}")
print(f"All cities visited: {all_cities}")

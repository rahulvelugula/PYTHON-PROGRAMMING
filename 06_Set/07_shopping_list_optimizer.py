"""
Question:
You are maintaining two shopping lists:
Home and Office.

Perform the following operations:

1. Find items common to both lists.

2. Find items unique to the Home list.

3. Find items unique to the Office list.

4. Find the combined unique list
   of all items without duplicates.

5. Display all result
"""

home = set(input().split())
office = set(input().split())

common = home & office

home_only = home - office
office_only = office - home

all_items = home | office

print(f"Items to buy for both: {common}")
print(f"Items only for home: {home_only}")
print(f"Items only for office: {office_only}")
print(f"All unique items: {all_items}")

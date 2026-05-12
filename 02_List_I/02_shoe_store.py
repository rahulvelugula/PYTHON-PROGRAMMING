"""
Question:
Maintain a shoe store inventory using lists.

Add a new shoe type,
remove an unwanted shoe type,
and check whether a requested shoe is available.
"""

shoes = input().split(", ")

add_shoe = input()
remove_shoe = input()
customer_choice = input()

shoes.append(add_shoe)

if remove_shoe in shoes:
    shoes.remove(remove_shoe)

print("Final list of shoes:", shoes)

if customer_choice in shoes:
    print(f"Yes, {customer_choice} are available in the store.")
else:
    print(f"Sorry, {customer_choice} are not available in the store.")

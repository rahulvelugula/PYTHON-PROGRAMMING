"""
Question:
You are managing a furniture store inventory.

Perform the following operations:

1. Create a dictionary with:
   - furniture names
   - amounts
   - prices

2. A customer buys 4 chairs.
   Update the chair quantity.

3. Add new items:
   - carpet
   - lamp

4. Remove all tables from inventory
   using different methods.

5. Print the final dictionary
   in aligned format.

6. Calculate the total value
   of furniture in storage.
   
"""

store = {
    "furniture": ["chair", "table", "sofa"],
    "amount": [24, 7, 6],
    "price": [200, 500, 1200]
}

#2
chair_index = store["furniture"].index("chair")
store["amount"][chair_index] -= 4

#3
store["furniture"].append("carpet")
store["amount"].append(9)
store["price"].append(150)

#3
store["furniture"] += ["lamp"]
store["amount"] += [4]
store["price"] += [180]

#4 : Remove table using pop()
table_index = store["furniture"].index("table")
store["furniture"].pop(table_index)

#4 : Remove amount and price using del
del store["amount"][table_index]
del store["price"][table_index]

#5
print("Updated Furniture Store:\n")
for key, value in store.items():
    print(f"{key:>10} : {str(value):<}")

#6
total = 0
for i in range(len(store["furniture"])):
    total += (
        store["amount"][i]
        * store["price"][i]
    )
print(f"\nTotal price of all furniture in storage: ₹{total}")

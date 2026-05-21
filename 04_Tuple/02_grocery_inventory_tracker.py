"""
Question:
Track grocery inventory using tuples.

Calculate the total bill,
update stock quantities,
and ignore purchases that exceed stock.

"""

n = int(input())
inventory = {}

for i in range(n):

    item, price, quantity = input().split()
    inventory[item] = (int(price), int(quantity))

m = int(input())
total_bill = 0

for i in range(m):

    item, purchased_quantity = input().split()
    purchased_quantity = int(purchased_quantity)

    if item in inventory:
        price, stock = inventory[item]

        if purchased_quantity <= stock:
            total_bill += price * purchased_quantity

            inventory[item] = (price, stock - purchased_quantity)

print("Total Bill:", total_bill)
print("Updated Inventory:")

# Display updated inventory
for item in inventory:
    price, quantity = inventory[item]
    print(item, price, quantity)

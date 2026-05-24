"""
Question:
You own a juice shop and want to manage
juice inventory using dictionaries.

Perform the following operations:

1. Create a list of juice dictionaries
   containing:
   - flavor
   - price
   - color

2. Add:
   - "in shop" status to each juice

3. Add a new juice:
   - grape juice

4. Calculate the average price
   of all juices.
   
"""

juices = [
    {"flavor": "orange", "price": 50, "color": "orange"},
    {"flavor": "lemon", "price": 40, "color": "yellow"},
    {"flavor": "pomegranate", "price": 70, "color": "red"}
]
#2
for juice in juices:
    juice["in shop"] = True
print("Initial juice list with 'in shop' status:")
print(juices)

#3
juices.append(
    {
        "flavor": "grape",
        "price": 60,
        "color": "purple",
        "in shop": True
    }
)
print("\nAfter adding new juice (grape):")
print(juices)

#4
total = 0
for juice in juices:
    total += juice["price"]
average = total / len(juices)
print("\nAverage price of juices:", average)

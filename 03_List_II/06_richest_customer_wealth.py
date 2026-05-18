"""
Question:
Find the wealth of the richest customer.
Customer wealth is the sum of all bank accounts.

"""

rows = int(input())

accounts = []

for i in range(rows):
    row = list(map(int, input().split()))
    accounts.append(row)

richest = 0

#Calculate the wealth of each customer
for customer in accounts:

    wealth = sum(customer)

    # Update richest wealth
    if wealth > richest:
        richest = wealth

print(richest)

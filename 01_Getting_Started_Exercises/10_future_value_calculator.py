"""
Question:
Calculate and display the future value
of an investment over a specified number of years.

Inputs:
1. Initial investment amount
2. Annual interest rate
3. Number of years

Display the investment value for each year.
"""

principal = float(input())
rate = float(input())
years = int(input())

print("Year\tValue")
print("----------------")

for year in range(years + 1):
    print(f"{year}\t${principal:.2f}")
    principal = principal * (1 + rate)

"""
Question:
Maintain a list of available currencies
and currencies to order.

If the requested currency is available:
- inform the customer
- remove it from available currencies
- add it to currencies to order

Otherwise:
- inform the customer
- add it to currencies to order

"""

available_currencies = input().split(", ")
order_currencies = input().split(", ")

currency = input()
#list methods
if currency in available_currencies:
    print(f"Yes, {currency} are available.")
    available_currencies.remove(currency)
    order_currencies.append(currency)
else:
    print(f"Sorry, {currency} are not available.")
    order_currencies.append(currency)

print("Updated available currencies:", available_currencies)
print("Updated currencies to order:", order_currencies)

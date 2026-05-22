"""
Question:
Calculate the final balance of each bank account
using transaction records stored as tuples.

"""
n = int(input())
balances = {}
for i in range(n):
    account_number, transaction_type, amount = input().split()
    account_number = int(account_number)
    amount = int(amount)
    record = (account_number, transaction_type, amount)

    if account_number not in balances:
        balances[account_number] = 0

    # Credit transaction
    if transaction_type == "credit":
        balances[account_number] += amount

    # Debit transaction
    else:
        balances[account_number] -= amount

# Check if transactions exist
if len(balances) == 0:
    print("No transactions found.")
else:
    # Display final balances
    for account in balances:
        print((account, balances[account]))

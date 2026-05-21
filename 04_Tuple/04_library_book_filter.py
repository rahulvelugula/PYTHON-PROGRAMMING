"""
Question:
Find all books published within
a given year range using tuples.

"""

n = int(input())
books = []

for i in range(n):

    title, author, year, copies = input().split()
    record = (title, author, int(year), int(copies))
    books.append(record)


start_year, end_year = map(int, input().split())
found = False

for book in books:

    title, author, year, copies = book
    if start_year <= year <= end_year:
        print(book)
        found = True

if found == False:
    print("No books found in the given range.")

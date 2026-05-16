"""
Question:
Perform inventory management operations
on a bookstore list using list methods.

"""

books = [
    "The Alchemist",
    "1984",
    "To Kill a Mockingbird",
    "The Great Gatsby",
    "Moby Dick"
]

print("Original list of books:", books)

#a
books.remove("1984")

print("\nAfter selling '1984':", books)

#b
books.append("Pride and Prejudice")
books.append("The Catcher in the Rye")

print("\nAfter adding new books:", books)

#c
print("\nTotal number of books:", len(books))

#d
print("First book:", books[0])
print("Last book:", books[-1])

#e
books.sort()

print("\nBooks sorted alphabetically:", books)

#f
if "Moby Dick" in books:
    print("\nYes, 'Moby Dick' is available in the store.")
else:
    print("\nNo, 'Moby Dick' is not available in the store.")

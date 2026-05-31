"""
Question:
You are given two articles.

Perform the following operations:

1. Find words common to both articles.

2. Find words unique to the first article.

3. Find words unique to the second article.

4. Find the total number of distinct
   words across both articles.

5. Ignore case and punctuation.

"""

article1 = input()
article2 = input()

for ch in ".,!?;:'\"":
    article1 = article1.replace(ch, "")
    article2 = article2.replace(ch, "")

words1 = set(article1.lower().split())
words2 = set(article2.lower().split())

common = words1 & words2

unique1 = words1 - words2
unique2 = words2 - words1

total_distinct = len(words1 | words2)

print(f"Common words: {common}")
print(f"Unique to first: {unique1}")
print(f"Unique to second: {unique2}")
print(f"Total distinct words: {total_distinct}")

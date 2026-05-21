"""
Question:
Remove all occurrences of a given value
from the array and return the count
of remaining elements.

"""

nums = list(map(int, input().split()))

val = int(input())

k = 0

for num in nums:
    if num != val:
        nums[k] = num
        k += 1

print("k =", k)
print("Updated array:", nums)

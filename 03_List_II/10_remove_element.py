"""
Question:
Remove all occurrences of a given value
from the array and return the count
of remaining elements.

"""

# Read list of numbers
nums = list(map(int, input().split()))

#Read value to remove
val = int(input())

k = 0

# Move non-val elements to front
for num in nums:

    if num != val:
        nums[k] = num
        k += 1

print("k =", k)
print("Updated array:", nums)

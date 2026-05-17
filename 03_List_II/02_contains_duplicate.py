"""
Question:
Check whether an array contains duplicate elements.
Return True if any value appears more than once,
otherwise return False.

"""

#Read list of numbers
nums = list(map(int, input().split()))

duplicate = False

# Compare every element with remaining elements
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):

        #Duplicate found
        if nums[i] == nums[j]:
            duplicate = True

print(duplicate)

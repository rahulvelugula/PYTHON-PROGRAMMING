"""
Question:
Find the majority element in an array.
The majority element appears more than n/2 times.

"""

nums = list(map(int, input().split()))
majority = 0

for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1

    if count > len(nums) // 2:
        majority = i
        break

print(majority)

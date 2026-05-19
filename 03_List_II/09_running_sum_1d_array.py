"""
Question:
Find the running sum of a 1D array.

"""

# Read list of numbers
nums = list(map(int, input().split()))

running_sum = []

total = 0

#calculate the running sum
for num in nums:

    total += num

    running_sum.append(total)

print(running_sum)

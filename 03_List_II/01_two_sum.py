"""
Question:
Find the indices of two numbers
whose sum is equal to the target value.

"""
#read list of numbers
nums = list(map(int, input().split()))
#read target value
target = int(input())
#check every pair of numbers
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      
        if nums[i] + nums[j] == target:
            print([i, j])
            break

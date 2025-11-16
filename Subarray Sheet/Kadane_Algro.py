# Problem Statement 
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    print(max_sum)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum(nums)

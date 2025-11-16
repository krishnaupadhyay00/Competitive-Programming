# Problem Statement 
# Given an array of integers, print the sum of all possible subarrays. 


def subarray_sums(arr):
    n = len(arr)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            print(total)
arr = [1, 2, 3]
subarray_sums(arr)

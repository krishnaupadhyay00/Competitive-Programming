# Problem Statement 
# Given an integer array, find the sum of all subarray sums using the Contribution Technique. 

def total_subarray_sum(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        contribution = arr[i] * (i + 1) * (n - i)
        total += contribution

    print(total)
arr = [1, 2, 3]
total_subarray_sum(arr)
    
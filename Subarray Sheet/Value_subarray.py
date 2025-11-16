# Problem Statement 
# Given an array of integers, print all possible subarrays and their elements.


def print_subarrays(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()
arr = [1, 2, 3, 4, 5]
print_subarrays(arr)

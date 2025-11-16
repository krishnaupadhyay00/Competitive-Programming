# Problem Statement 
# Given an integer array and two indices L and R, find the sum of elements between those indices (inclusive)

# Function to find sum of elements from index L to R
def subarray_sum(arr, L, R):
    total = 0
    for i in range(L - 1, R):  
        total += arr[i]
    print(total)
arr = [1, 2, 3, 4, 5]
L, R = 2, 4
subarray_sum(arr, L, R)

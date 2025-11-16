# Problem Statement: Given an integer N representing the number of elements in an array, 
# find the total number of subarrays that can be generated from it.

def total_subarrays(n):
    total = (n * (n + 1)) // 2
    print("Total Subarrays:", total)

N = 4
total_subarrays(N)

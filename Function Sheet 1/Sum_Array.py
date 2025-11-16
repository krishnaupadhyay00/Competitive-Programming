#  Write a program to print sum of elements of the input array A of size N.

def sum_array(arr):
    total = 0
    for i in arr:
        total += i
    return total
print(sum_array([1,2,3,4,5]))

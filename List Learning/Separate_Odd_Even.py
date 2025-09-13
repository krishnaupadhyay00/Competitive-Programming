#You are given an integer array A. You have to print the odd and even elements of array A in 2 separate lines.

A = [1, 2, 3, 4, 5,]  
for num in A:
    if num % 2 != 0:
        print(num, end=" ")
print()  
for num in A:
    if num % 2 == 0:
        print(num, end=" ")
print()  

# // Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as
# // input from user
# // Input:- N = 10
# // Output:- 55



N = int(input("Enter a positive integer: "))

sum_numbers = 0
i = 1
while i <= N:
    sum_numbers += i
    i += 1

print("Sum of natural numbers from 1 to", N, "is:", sum_numbers)

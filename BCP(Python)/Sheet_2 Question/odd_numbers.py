# 4. Write a program to print all odd numbers from 1 to N, where you have to take N as input
# from user.
# Input:- N = 10
# Output:- 1 3 5 7 9

N = int(input("Enter the number: "))

i = 1
while i <= N:
    print(i, end=" ")
    i += 2

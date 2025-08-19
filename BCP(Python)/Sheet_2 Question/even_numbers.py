#  3. Write a program to print all even numbers from 1 to N, where you have to take N as input
# from the user.
# Input:- N = 10
# Output:- 2 4 6 8 10

N = int(input("Enter the number: "))

i = 2
while i <= N:
    print(i, end=" ")
    i += 2

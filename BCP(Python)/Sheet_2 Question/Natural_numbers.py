# 2. Write a program to print all Natural numbers from N to 1, where you have to take N as input
#from the user.
#Input:- N = 5
#Output:- 5 4 3 2 1

N = int(input("Enter the number: "))

i = N
while i >= 1:
    print(i, end=" ")
    i -= 1

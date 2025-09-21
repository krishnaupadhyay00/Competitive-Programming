#Write a program to print all negative numbers from input array A of size N

N = int(input())
A = list(map(int, input().split()))
for num in A:
    if num < 0:
        print(num)


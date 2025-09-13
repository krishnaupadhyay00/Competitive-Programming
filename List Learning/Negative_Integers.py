#Write a program to print all negative numbers from input array A of size N

N = int(input("Enter size of array: "))
A = list(map(int, input("Enter elements: ").split()))
for x in A:
    if x < 0:
        print(x)

#You are provided with an integer array A. Return another array B of size same as that of A such that B[i] = A[i]^3

n=int(input("Enter the size of array:"))
a=list(map(int,input().split()))
b=[num**3 for num in a]
print("Cubde Array",b)
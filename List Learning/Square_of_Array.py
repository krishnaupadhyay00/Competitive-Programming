#You are provided with an integer array A. Return another array B of size same as that of A such that B[i] = A[i]^2

n=int(input("Enter the size of array:"))
a=list(map(int,input().split()))
b=[num**2 for num in a]
print("Squard Array:",b)
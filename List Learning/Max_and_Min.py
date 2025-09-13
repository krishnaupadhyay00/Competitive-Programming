#Take input an array A of size N and write a program to print maximum and minimum
#elements of the input array .Here N represents the length of the array .

N = int(input("Enter size of array: "))
A = list(map(int, input("Enter elements: ").split()))
max = A[0]
min = A[0]
for i in range(1, N):
    if A[i] > max:
        max = A[i]
    if A[i] < min:
        min = A[i]
print("Maximum element:", max)
print("Minimum element:", min)



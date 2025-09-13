#Given two lists A1 and A2, each containing integers, write a Python program to compute the element-wise sum of the 
# corresponding elements in the two lists and store the resultin a new list.

n = int(input("Enter the size of both list: "))
A1 = list(map(int, input("Enter the first element:").split()))
A2 = list(map(int, input("Enter the second element ").split()))
B = []
for i in range(n):
    B.append(A1[i] + A2[i])
print("Element-wise sum list:", B)

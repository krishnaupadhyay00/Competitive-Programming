# Write a program to reverse the words present in a string. Check example input/output.
A = input("Enter a string:")
w = A.split()
for i in w:
    print(i[::-1], end=" ")
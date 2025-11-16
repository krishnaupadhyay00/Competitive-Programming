#  You are given string (A) and you have to print after reversing that

# A = input("Enter a string:")
# print(A[::-1])


A = input("Enter a string: ")
rev = ""
for ch in A:
    rev = ch + rev
print("Reversed string:", rev)

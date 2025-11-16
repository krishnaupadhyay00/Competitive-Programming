#  You are given a character string A, having length N and an integer ASCII code B.
#  You have to tell the leftmost occurrence of the character having ASCII code equal to B, in A or
#  report that it does not exist.

A = input("Enter a string:")
B = int(input("Enter ASCII code:"))
if chr(B) in A:
    print(A.index(chr(B)))
else:
    print("-1")
    
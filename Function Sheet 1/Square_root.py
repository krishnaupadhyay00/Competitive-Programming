#  Given a number A. Return square root of the number if it is perfect square otherwise return-1.
#  Note: A number is a perfect square if its square root is an integer.

import math

def square_root(A):
    sqrt = math.sqrt(A)       
    if sqrt.is_integer():     
        return int(sqrt)     
    else:               
        return -1              

num = int(input("Enter a number: "))
result = square_root(num)
print("Result:", result)
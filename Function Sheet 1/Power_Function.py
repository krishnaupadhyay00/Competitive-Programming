#  You are given two integers A and B.You have to find the value of A^B.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
print(power(2,5))
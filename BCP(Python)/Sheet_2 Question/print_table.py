# 1. Take a number A as input, print its multiplication table having the first 10 multiples.

A = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(A, "x", i, "=", A * i)
    i += 1

# 12. You are given two integers A and B. You have to find the value of A^B.
# Input:- A = 2 , B = 3
# Output:- 8
# Explaination:- For A=2 and B=3, the value of 2^3 = 2 * 2 * 2 = 8.

A = int(input("Enter the base (A): "))
B = int(input("Enter the exponent (B): "))

result = 1
count = 1

while count <= B:
    result *= A
    count += 1

print(f"{A} raised to the power {B} is: {result}")

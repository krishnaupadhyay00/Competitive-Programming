#1. Find Minimum of 3 Numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    minimum = a
elif b < a and b < c:
    minimum = b
else:
    minimum = c

print("Minimum number is:", minimum)
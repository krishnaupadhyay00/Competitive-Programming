# Problem: 
# Write a recursive function to find the factorial of a number.

n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)

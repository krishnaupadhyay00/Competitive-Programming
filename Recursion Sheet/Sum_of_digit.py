# Problem: 
# Find the sum of the digits of a given number using recursion.

n = 1234   
sum = 0

while n > 0:
    digit = n % 10       
    sum += digit         
    n = n // 10          
print("Sum of digits:", sum)

 
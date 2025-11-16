# Problem: 
# Write a recursive function to count the digits in a number. 
def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)
print(count_digits(12345))

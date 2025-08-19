# 9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the
# given number N.
# Input:- N = 1589
# Output:- 23
# Explaination:- For the number 1589, the digits are 1,5,8,9. The Sum(1589) = 1+5+8+9 = 23.



N = int(input("Enter a number: "))

sum_digits = 0
num = N

while num > 0:
    digit = num % 10      # Last digit nikalte hain
    sum_digits += digit   # Us digit ko sum mein add karte hain
    num = num // 10      # Last digit hata dete hain

print("Sum of digits of", N, "is:", sum_digits)

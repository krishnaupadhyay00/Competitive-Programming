# Input number
A = int(input("Enter a number: "))

# Check divisibility by both 5 and 11
if A % 5 == 0 and A % 11 == 0:
    print("YES, the number is divisible by both 5 and 11.")
else:
    print("NO, the number is not divisible by both 5 and 11.")

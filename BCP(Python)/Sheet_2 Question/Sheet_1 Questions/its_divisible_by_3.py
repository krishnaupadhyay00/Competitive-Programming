#Q5. Read a number check if its divisible by 3 or its last digit is 4.

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 10 == 4:
    print("YES, the number is divisible by 3 and the last digit is 4.")
else:
    print("NO, the number does not satisfy both conditions.")


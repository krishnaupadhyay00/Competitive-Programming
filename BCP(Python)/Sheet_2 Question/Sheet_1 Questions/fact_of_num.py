#Q1 Print all factors/divisor of a given +ve number.

'''num = int(input("Enter a positive num:"))

i=1
print(f"Factors of{num} are:")
while i<=num:
  if num % i == 0:
   print(i)
   i +=1'''


#Q2. Read N, Print No of digits in N

N = int(input("Enter a number: "))
num = (N)
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10
        count += 1

print(f"Number of digits in {N} is: {count}")



# // 8. Take an integer N as input and print the count of digits of that number.
# // Input:- N = 10101
# // Output:- 5
# // Explanation:- 10101 has 5 digits

N = int(input("Enter a number: "))

count = 0
num = N

if N == 0:
    count = 1
else:
    while num != 0:
        num = num // 10    
        count += 1

print("Number of digits in", N, "is:", count)



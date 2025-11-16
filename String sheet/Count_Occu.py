#  Find the number of occurrences of bob in string A consisting of lowercase English alphabets

# A = input("Enter a string:")
# print(A.count("bob"))A = input("Enter a string: ")




A = input("Enter a string:")
count = 0
i = 0
while i < len(A) - 2:
    if A[i:i+3] == "bob":
        count += 1
    i += 1

print(count)






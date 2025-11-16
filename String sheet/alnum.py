# Print 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, print 0.

A = input("Enter a string:")
if A.isalnum():
    print("1")
else:
    print("0")
# Problem: 
# Using recursion, check whether a string is a palindrome or not. 

s = "madam"   
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

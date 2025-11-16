# Problem: 
# Write a recursive function to reverse a string. 
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:])+ s[0]
print(reverse_string("Hello"))
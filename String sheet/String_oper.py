# Concatenate string with itself

# Delete all uppercase letters

# Replace each vowel with #

A = input("Enter string: ")
A = A + A        #Concatenate string with itself
result = ""       #Remove uppercase and replace vowels
for ch in A:
    if ch.isupper():          # skip uppercase letters
        continue
    elif ch in 'aeiou':       # replace vowels with #
        result += '#'
    else:
        result += ch

print(result)

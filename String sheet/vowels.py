# Write a program to input T strings(S) from user and print count of vowels and consonants in it 

T = int(input("Enter number of strings: "))

for i in range(T):
    s = input("Enter string: ")
    vowels = 0
    consonants = 0

    for ch in s.lower():
        if ch in 'aeiou':
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

        
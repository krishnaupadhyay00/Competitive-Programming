# Write a Python program that defines a function fun(a) which takes an integer a as input and returns
#  True if a is even, otherwise it returns False. Then, create a list called sequence containing integers
#  and floating-point numbers. Use the filter() function along with the fun function to filter out the
#  even numbers from the sequence list, and store the filtered values in a new list called filtered.
#  Finally, print the filtered list

def fun(a):
    return a % 2 == 0   
sequence = [10, 3.5, 20, 15.2, 8, 9, 12.0, 7.4, 14]
filtered = list(filter(fun, sequence))
print("Filtered even numbers:", filtered)

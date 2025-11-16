# Accepts an integer input from the user and stores it in a variable num.
# Defines a lambda function even_odd_No that takes one parameter num and returns "even"
# if num is even, otherwise it returns "odd".
# The lambda function is defined inside a regular function check_even_odd.

def check_even_odd(num):
    even_odd_No = lambda num: "even" if num % 2 == 0 else "odd"
    return even_odd_No(num)
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(result)

#  Write a Python program that utilizes the map, filter, and lambda functions to achieve the following
#  objectives:
#  Use map to convert a list of integers to their corresponding squares.
#  Use filter to keep only the squared numbers that are multiples of a specific number

def process_numbers(numbers, n):
    squares = list(map(lambda x: x ** 2, numbers))
    result = list(filter(lambda x: x % n == 0, squares))
    
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5 
output = process_numbers(numbers, n)
print(output)

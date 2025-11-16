# Write a single line of Python code that accepts a list of integer values from the user, filters out
#  the numbers greater than 60 using the filter() function with a lambda function, and stores the
#  filtered values in a variable ans. Print the ans list.

def filter_greater_than_60(nums):
    return list(filter(lambda x: x > 60, nums))

arr = list(map(int, input("Enter numbers separated by space: ").split()))
ans = filter_greater_than_60(arr)
print(ans)

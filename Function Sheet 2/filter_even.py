#  Define a list arr containing integer values.
#  Use the filter() function with a lambda function to filter out the even numbers from the list
#  arr.
#  Store the filtered values in a variable ans.
#  Print the filtered list

def filter_even_numbers(arr):
    filtered_list = list(filter(lambda x: x % 2 == 0, arr))
    return filtered_list
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(arr)
print("Filtered even numbers:", filtered_list)

#  Define a list arr containing integer values.
#  Use the map() function with a lambda function to add 10 to each element of the list arr.
#  Store the modified values in a variable ans.
#  Print the ans list

def add_ten_to_each_element(arr):
    return list(map(lambda x: x + 10, arr))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = add_ten_to_each_element(arr)
print("Modified list:", result)

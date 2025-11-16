#  Define a list names containing string values.
#  Use the map() function with a lambda function to convert each name in the list names to
#  lowercase.
#  Store the modified names in a variable result.
#  Print the result list.

def convert_to_lower(names_list):
    return list(map(lambda name: name.lower(), names_list))
names = ["Suyash", "CHAUDHARY", "Krishna", "PYTHON"]
result = convert_to_lower(names)
print(result)
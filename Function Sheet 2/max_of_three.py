# Define a lambda function max_of_three that takes three parameters a, b, and c, and
# returns the maximum of the three values.
#  Call the lambda function max_of_three with three integer values

def max_of_three(a, b, c):
    max_of_three = lambda x, y, z: x if x > y and x > z else (y if y > z else z)
    return max_of_three(a, b, c)
result = max_of_three(10, 25, 15)
print("Maximum value is:", result)

# Output: Maximum value is: 25

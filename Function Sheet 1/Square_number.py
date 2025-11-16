#  WAP to print square of all numbers from x to y.

def print_squares(x, y):
    for i in range(x, y + 1):
        print(f"Square of {i} is {i * i}")
x = 1
y = 5
print_squares(x, y)

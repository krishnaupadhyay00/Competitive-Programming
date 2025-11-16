# WAP to make a calculator by using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("Operations: +, -, *, /")

a = 10
b = 5
op = '*'

if op == '+':
    print("Result:", add(a, b))
elif op == '-':
    print("Result:", subtract(a, b))
elif op == '*':
    print("Result:", multiply(a, b))
elif op == '/':
    print("Result:", divide(a, b))
else:
    print("Invalid Operator!")
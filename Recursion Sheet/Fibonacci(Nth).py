# Problem: 
# Write a recursive function to find the Nth Fibonacci number. 

def fibonacci(n):
    if n <= 1:     
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
N = 6
print(fibonacci(N))

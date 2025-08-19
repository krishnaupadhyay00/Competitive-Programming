#Reverse of numbers

N = int(input("Enter a number: "))

reverse = 0
while N > 0:
    digit = N % 10          
    reverse = reverse * 10 + digit  
    N //= 10                          #last digit hata dega

print("Reverse of number:", reverse)
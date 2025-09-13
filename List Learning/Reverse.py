#Given an array A, Find the reverse of it. (Solve this question with for loop)

A = [3,5,1,2,1,2]    
B = []                  
for i in range(len(A)-1, -1, -1):
    B.append(A[i])

print("Reversed array:", B)

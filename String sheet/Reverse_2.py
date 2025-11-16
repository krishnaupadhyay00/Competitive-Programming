# You are given string (A) and you have to print the reverse order of words

A = input("Enter e string ")
w=A.split()
for i in range(len(w)-1,-1,-1):
    print(w[i],end=" ")
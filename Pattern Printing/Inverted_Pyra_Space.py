# *_ _ _ _ _*
# *_ _ _ _*
# *_ _ _*
# *_ _*
# *_*

n=int(input())
for i in range(1,n+1):
    print("*", end=" ")
    for j in range(n-i+1):
        print("_", end=" ")
    print("*",end=" ")
    print()

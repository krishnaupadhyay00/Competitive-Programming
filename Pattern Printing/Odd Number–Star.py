# 1
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        if j%2==0:
            print(j+1, end=" ")
        else:
            print("*", end=" ")
    print()
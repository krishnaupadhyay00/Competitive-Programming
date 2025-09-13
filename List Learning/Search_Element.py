#You are given array A and an integer B. You have to tell whether B is present in array A
#or not.

A = [1, 5, 9, 1]
B = 5
found = 0
for x in A:
    if x == B:
        found = 1
        break
print(found)


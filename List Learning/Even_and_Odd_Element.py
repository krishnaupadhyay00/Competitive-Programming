#For array A, you have to find the value of absolute difference between the counts of
#even and odd elements in the array.

A = [1,2,3,4] 

count_even = 0
count_odd = 0

for num in A:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

abs_diff = abs(count_even - count_odd)
print("Absolute difference:", abs_diff)


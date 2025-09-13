list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

print(len(list))
#Output:  11


print(list[-2 :-5: -1])
#Output:  [19, 17, 15]


print(list[-2:])
#Output:  [19, 21]


print(list[-2::])
#Output:  [19, 21]


print(list[:-2])
#Output:  [1, 3, 5, 7, 9, 11, 13, 15, 17]


print(list[::-2])
#Output:  [21, 17, 13, 9, 5, 1]


print(list[::-1])
#Output:  [21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
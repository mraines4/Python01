# given  two-dimensional lists of numbers the size of 2x2
# calculate teh result of adding the 2 matricies

list1 = [
    [1, 3, 4],
    [4, 6, 5]
]

list2 = [
    [2, 7, 6],
    [9, 4, 6]
]

matrix = [
    [],
    []
]

result1 = []
result2 = []

index = 0
sublength = len(list1[0])

for sublist in list1:
    for integer in sublist:
        result1.append(integer)

for sublist in list2:
    for integer in sublist:
        result2.append(integer)

length = len(result1)

for i in range(length):
    matrix[index].append(result1[i] + result2[i])
    if len(matrix[index]) == sublength:
        index +=1

print(matrix)
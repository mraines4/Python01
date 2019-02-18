# given 2 lists the same length, create new list by mult the pairs in same postition

numbers1 = [16, 2, 3, -8, 5, 10]
numbers2 = [5, 6, 3, 55, -5, 7]
new_list = []
index = 0

for first in numbers1:
    new_list.append(first * numbers2[index])
    index += 1

print(new_list)


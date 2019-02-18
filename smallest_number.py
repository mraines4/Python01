numbers = [16, 2, 3, 8, 5, 10]

small = numbers[0]
for i in numbers:
    if i < small:
        small = i
print(small)
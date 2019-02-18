numbers = [16, 2, 3, 8, 5, 10]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
print(largest)
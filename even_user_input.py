user_input = input('please enter numbers: ')

array = user_input.split(' ')

new_array = []

for number in array:
    new_array.append(int(number))

for i in new_array:
    if (i % 2 == 0):
        print(i)
        
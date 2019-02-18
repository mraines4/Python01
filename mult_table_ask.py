# make multiplication table from 1 through 10

# left_number = 1


# while left_number < 11:
#     right_number = 1
#     while right_number < 11:
#         total = left_number * right_number
#         print('%d * %d = %d' % (left_number, right_number, total))
#         right_number = right_number + 1
#     left_number = left_number + 1


user_input = int(input('Gimme a number '))

def multi_table(number):
    right_number = 1
    while right_number < 11:
        total = number * right_number
        print('%d * %d = %d' % (number, right_number, total))
        right_number += 1

multi_table(user_input)
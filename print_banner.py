# print a string with a * box around it the size of the string

user_input = input('Text? ')

length = len(user_input) + 4
input = True

while input:
    print('*' * length)
    print('* ' + user_input + ' *')
    print('*' * length)
    input = False

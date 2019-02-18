# print a triangle of *

# star = 1
# star_power = ('*')
# spacer = (' ')
# space_counter = 3

# while star < 5:
#     print((spacer * str(space_counter)) + (star_power * str(star)) + (spacer * str(space_counter)))
#     star = star + 1
#     spacer = spacer - 1


user_height = int(input("height? "))
line_counter = 0
spacer = ' '
star = '*'

while line_counter < user_height:
    if line_counter < user_height:
        line_spacer = spacer * (user_height - line_counter)
        star_counter = star + (star * (line_counter)) * 2
        print('%s%s' % (line_spacer, star_counter))
        line_counter += 1
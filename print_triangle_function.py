# print a triangle of *



user_height = int(input("height? "))

def funny(x):
    line_counter = 0
    spacer = ' '
    star = '*'

    while line_counter < user_height:
        if line_counter < user_height:
            line_spacer = spacer * (user_height - line_counter)
            star_counter = star + (star * (line_counter)) * 2
            print('%s%s' % (line_spacer, star_counter))
            line_counter += 1

funny(user_height)




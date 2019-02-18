# give height and width from user, print a box of * as a border
# line 1 print out
# line next through second to last print first and last space
# last line print out

width = int(input('Width? '))
height = int(input('Height? '))

def BoxyBox(W, H):
    lines = 0
    while lines < height:
        if lines == 0:
            print('*' * width)
            lines = lines + 1
        elif lines < height - 1:
            spacer = ' ' * (width - 2)
            print('*'+ spacer + '*')
            lines = lines + 1
        elif lines == height -1:
            print('*' * width)
            lines = lines + 1

BoxyBox(width, height)


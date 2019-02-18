# print first 100 triangle numbers

dots = 1

while dots < 101:
    triangle = dots * (dots + 1)/2
    print (int(triangle))
    dots += 1

# print a NxN square of *
# prompt for N

# num_of_lines = int(input('How big is the square? '))

# def Squarysquare(numb):
#     lines = 0
#     while lines < numb:
#         lines = lines + 1
#         print ('*' * numb)

# Squarysquare(num_of_lines)

num_of_lines = int(input('How big is the square? '))

# def Squarysquare(numb):
#     placey_place = ''
#     lines = 0
#     while lines < numb:
#         lines = lines + 1
#         if lines == numb:
#             placey_place += ('*' * numb)
#         else:
#             placey_place += ('*' * numb) + '\n'

#     return placey_place

# print(Squarysquare(num_of_lines))

def Squarysquare(numb):
    placey_place = ''
    lines = 0
    while lines < numb:
        lines = lines + 1
        placey_place += ('*' * numb) + '\n'
    return placey_place.rstrip()

print(Squarysquare(num_of_lines))
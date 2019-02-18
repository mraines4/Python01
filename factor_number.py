# given a number, print its factors

user_input = int(input('Gimme a number fool: '))
factor = 1

while factor < user_input:
    if user_input % factor == 0:
        print(factor)
    factor += 1
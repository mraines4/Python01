thingy = "happy birthday cheezit"

new_string = ''
index = 0

doubles = ['a', 'e', 'i', 'o', 'u']

for char in thingy:
    if char in doubles:
        if thingy[index] == thingy[index+1]:
            new_string += char * 4
        else:
            new_string += char
    else:
        new_string += char
    index += 1

print(new_string)


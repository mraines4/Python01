thingy = "what is up chicken butt"

# print(thingy[::-1])

new_string = ''
length = len(thingy)

for letter in range(length, 0, -1):
    index = letter - 1
    new_string += thingy[index]
print(new_string)


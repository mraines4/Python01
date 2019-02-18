thingy = "what is up chicken butt"


# capitalized = string.capitalize()

# print(capitalized)
returned = ''
index = 0

# first_letter = thingy[0].upper()
# print(thingy)

for i in thingy:
    if index == 0:
        returned += i.upper()
    else:
        returned += i
    index =+ 1
print(returned)

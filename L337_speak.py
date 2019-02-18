# thingy = "what is up chicken butt"

# capital = thingy.upper()

# leet = ''
# for letter in capital:
#     if letter == 'A':
#         leeted = '4'
#         leet += leeted
#     if letter == 'E':
#         leeted = '3'
#         leet += leeted
#     if letter == 'G':
#         leeted = '6'
#         leet += leeted
#     if letter == 'I':
#         leeted = '1'
#         leet += leeted
#     if letter == 'O':
#         leeted = '0'
#         leet += leeted
#     if letter == 'S':
#         leeted = '5'
#         leet += leeted
#     if letter == 'T':
#         leeted = '7'
#         leet += leeted
#     else:
#         leet += letter

# print(leet)

phrase = "Cats love fast vacuums"
upper = phrase.upper()
translation = ''
leet = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
l337 = ['4', '3', '6', '1', '0', '5', '7']
for letter in upper:
    if letter in leet:
        translation += l337[leet.index(letter)]
    if letter not in leet:
        translation += letter
print(translation)
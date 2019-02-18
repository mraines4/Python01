# plaintext = 'abcdefghijklmnopqrstuvwxyz '
# ciphertext= 'bcdefghijklmnopqrstuvwxyza '

# thingy = "this is a secret code!"

# lower = thingy.lower()

# cipher = ''


# for char in lower:
#     if char in ciphertext:
#         cipher += ciphertext[plaintext.index(char)]
#     else:
#         cipher += char

# print(cipher)

text = input("enter string: ")
s = int(input("enter shift number: "))


def encrypt(string, shift):
    cipher = ''
    for char in string: 
        if  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher = cipher + char

    return cipher

print("original string: ", text)
print("after encryption: ", encrypt(text, s))
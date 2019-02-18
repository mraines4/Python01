name = input('What is your name? '.upper())

message = 'Hello, %s!' % name
message2 = 'Your name %d letters in it! Awesome!' % len(name)

print(message.upper())
print(message2.upper())

import madlib_functions

print(madlib_functions.make_madlib(message, message))
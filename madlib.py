# prompt user for missing words

###################
# WITH A FUNCTION #
###################
# print('Please fill in the blanks below')
# name = "____(name)____"
# subject = '____(subject)____'

# def Madlib():
#     madlib = "%s's favorite subject in school is %s." % (name, subject)
#     print(madlib)

# Madlib()

# name = input("What is name? ")
# subject = input("what is subject? ")

# Madlib()


print("Please fill in the blanks below \n ____(name)____'s favorite subject in school is ____(subject)____.")

name = input("What is name? ")
subject = input("what is subject? ")

print("%s's favorite subject in school is %s." % (name, subject))

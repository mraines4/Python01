# prompt user for missing words

#########################
# WITH A FUNCTION Matt #
#########################
# print('Please fill in the blanks below')
# user_name = "____(name)____"
# user_subject = '____(subject)____'

# def Madlib(name, subject):
#     madlib = "%s's favorite subject in school is %s." % (name, subject)
#     print(madlib)

# Madlib()

# user_name = input("What is name? ")
# user_subject = input("what is subject? ")

# Madlib()


print("Please fill in the blanks below \n ____(name)____'s favorite subject in school is ____(subject)____.")

user_name = input("What is name? ")
user_subject = input("what is subject? ")

def make_madlib(name, subject):
    return "%s's favorite subject in school is %s." % (name, subject)

print(make_madlib(user_name, user_subject))



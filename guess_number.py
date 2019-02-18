# initialize secret number

# get user number

# compare user number to secret number

# if correct he wins

# if not prompt for another number
option = True
while option:
    import random
    secret_number = random.randint(1, 10)

    guessing = True
    print('I am thinking of a number between 1 and 10. Can you guess it?')
    guesses_left = 4
    while guessing:
        guess = int(input('Guess: '))
        if guess == secret_number and guesses_left >= 0:
            print('Holey Moley how did you know!!!')
            guessing = False
        elif guess > secret_number and guesses_left > 0:
            print('Too High!\nYou have %d guesses left' % guesses_left)
            guesses_left = guesses_left - 1
        elif guess < secret_number and guesses_left > 0:
            print('Too Low!\nYou have %d guesses left' % guesses_left)
            guesses_left = guesses_left - 1
        else:
            print('too bad so sad you lose!')
            guessing = False

    ans = True
    while ans:
        again = input('do you want to play again? (Y or N) ').lower()
        if again == 'y':
            ans = False
            option = True
        elif again == 'n':
            print("see ya!")
            ans = False
            option = False
        else:
            print("incorrect answer")
            option = False
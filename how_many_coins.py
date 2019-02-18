# # prompt how many coins you want
# # initialize to 0 coins
# ask if you want a coin
# if yes give one coin and print out current 
# if no stop program

coins = 0

coin_add = True
while coin_add:
    print('You have %d coins' % coins)
    coin_ask = input('Do you want a coin? ')
    if coin_ask == 'yes':
        coins = coins + 1
    elif coin_ask == 'no':
        print('Bye Felicia, you lost all your money!')
        coin_add = False
    else:
        print('you know nothing John Snow')
        coin_add = False
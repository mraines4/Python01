appropriate_meal = {
    'drink': 'Creature Comforts Athena',
    'appetizer' : 'charcuterie',
    'dinner': 'Grindhouse burger',
    'dessert': 'cupcakes'
}

house = {
    'kitchen': 'Fancy Refrigerator',
    'bathrooms': 3,
    'bedrooms': 4,
    'living room': 'giant'
}

user = {
    'firstName': 'Sean',
    'lastName': 'Reid'
}

# print(appropriate_meal['dessert'])
# print(house['kitchen'])
# print(user['firstName'])

# print('%s would like %s from the %s' % (user['firstName'], appropriate_meal['dessert'], house['kitchen']))

# if 'appetizer' in appropriate_meal:
#     print('WE HAVE HAM')
# else:
#     print('No ham, womp womp')

print(appropriate_meal)

appropriate_meal['water'] = 'tap'
appropriate_meal['bread'] = True
appropriate_meal['drink'] = 'Guinness'

print(appropriate_meal)

del appropriate_meal['water']

print(appropriate_meal)



digitalcrafts = {
    'US': {
        'Georgia': {
            'Atlanta': '3423 Piedmont Rd NE #420'
        },
        'Texas': {
            'Houston': '3302 Canal St.'
        }
    }
}

# print(digitalcrafts)

# digitalcrafts['US']['Florida'] = {}
# digitalcrafts['US']['Washington'] = {'Seattle': '123 main street'}
# digitalcrafts['Canada'] = {'British Columbia': {'Vancouver': '123 Queen Mary St.'}}

# print(digitalcrafts)

countries = digitalcrafts.keys()
us_states = digitalcrafts['US'].keys()

# print(countries)
# print(us_states)

# def us_cities(states):
#     cities = []
#     for key in states:
#         cities.append(digitalcrafts['US'][key])
#     return cities

# print(us_cities(us_states))


# def us_cities(states):
#     for key in states:
#         print('there are campuses in %s' % key)

# us_cities(us_states)

# state_dicts = digitalcrafts.values()

# print(state_dicts)

for country in digitalcrafts:
    for state in digitalcrafts[country]:
        print(country, state, end=': ')
        for city in digitalcrafts[country][state]:
            print(city)
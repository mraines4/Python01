user_input = input('Please enter a word: ')

count_dict = {}

for char in user_input:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1


print(count_dict)
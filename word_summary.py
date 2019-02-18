user_input = input('Please enter a sentence: ')

lowered = user_input.lower()
spliced_sentence = lowered.split()

count_dict = {}

for word in spliced_sentence:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1


print(count_dict)
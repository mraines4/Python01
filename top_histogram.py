user_input = input('Please enter a sentence: ')

lowered = user_input.lower() # convert all to lowercase
spliced_sentence = lowered.split() # split into individual words

count_dict = {} # initiate histogram dictionary

for word in spliced_sentence: 
    if word in count_dict:
        count_dict[word] += 1 # if word is already in new dictionary, increase the value by 1
    else:
        count_dict[word] = 1 # if its not already in the dictionary, add it and set value to 1

# print(count_dict)

# set self destruct dictionary
self_destruct = count_dict

# to print the top 3 words and their values
counter = 0 
while counter < 3:
    max_val = max(self_destruct, key=self_destruct.get) # this gets you the key with the highest value
    print('%s: %d' % (max_val, self_destruct[max_val])) #this will print the key and its value
    del self_destruct[max_val] # this deletes that key from the dictionary, making it start over until it gets the highest 3
    counter += 1



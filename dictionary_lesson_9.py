def count_dict():
    words = {}
    value = input("Please enter a word (press -999 to quit): ")

    while value != '-999':
        if value in words:
            words[value] = words[value] + 1
        else:
            words[value] = 1
        value = input("Please enter a word (press -999 to quit): ")

    temp_list = []
    # select a key in the dictionary
    for i in words.keys():
        #determine the number of words in the sorted list
        list_length = len(temp_list)

        #start looking at position 0
        placeholder = 0

        #as long as there are still items in the list

        while placeholder < list_length:
            #get the word in the sorted list
            list_key = temp_list[placeholder]

            #determine if this word has been entered
            #more times than the current word

            if words[list_key] > words[i]:
                break

            #it wasnt, so look at the next word in the sorted list
            placeholder = placeholder + 1
        #insert word in to sorted list
        temp_list.insert(placeholder, i)
        
    for i in words.keys():
        print(i, '\t', words[i])

# loops through the a string and extracts words from a word list
# for i in word list
#   string[:len(i)+1]
#   then add one to the starting point and ending point until you reach the end of the string
#   repeat until every word in word list in through
# apply same thing to cribs

# later implement in c language to speed things up

# used for when the code isn't in the actual length of the word instead in groups of 4 or 5

import time
import dictionaryload

word_list = dictionaryload.load('2of4brif.txt')

start_time = time.time()
def word_finder(string):
    words = {}
    string.replace(" ", "")
    for i in word_list:
        if i in string:
            words[i]= (string.find(i), string.find(i)+len(i)-1)
    
    return words

# print(word_finder("iwanttoeatfood"))
def word_joiner(word_dict, string):
    completed = False
    final = {}
    spaces = 0
    while not completed:
        for word, pos in word_dict.items():
            print(word_finder(string[:pos[0]+spaces]+string[pos[1]+1+spaces:]))
            print({key:val for key, val in word_dict.items() if key != word})
            print(string[:pos[0]+spaces]+string[pos[1]+1+spaces:])
            # checks if the amount of words present is more than 2 less after removing one of the potential words
            # if so it means its one of the actual words
            # use path finding like in go project
            if {key:val for key, val in word_dict.items() if key != word}.keys() == word_finder(string[:pos[0]+spaces]+string[pos[1]+1+spaces:]).keys():
                print(word)
                if not word in final.keys():
                    final[word]=pos
                    string = string[:pos[1]+1+spaces] + " " + string[pos[1]+1+spaces:]
                    spaces += 1
            else:
                print("flase", word)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(final)
        print(string)
        
        
print(word_joiner(word_finder("iwanttoeatfood"), "iwanttoeatfood"))
print("--- %s seconds ---" % (time.time() - start_time))
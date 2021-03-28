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

def get_key(val, dict):
    for key, value in dict.items():
         if val == value:
             return key

# print(word_finder("iwanttoeatfood"))

def searcher(dict):
    

def word_joiner(word_dict, string):
    completed = False
    final = ""
    
    starts = sorted(list(word_dict.values()), key = lambda x: x[0]) 
    ends = sorted(list(word_dict.values()), key = lambda x: x[1])
    print(starts)
    index = 0
    future= {}
    while not completed:
        
        
        pos_words = [i for i in starts if i[0] == index]
        next_pos = [i for i in starts if i[0] == index+1]
        
        print(pos_words)
        print(index)
        if len(pos_words) == 1:
            index += len(get_key(pos_words[0], word_dict))
            final += get_key(pos_words[0], word_dict)
        
        else: 
            for i in pos_words:
                future[i] = [j for j in ends if j[0] == i[1]+1]
            print(future)

        if index >= len(string):
           return final  

           
        
print(word_joiner(word_finder("iwanttoeatfood"), "iwanttoeatfood"))
print("--- %s seconds ---" % (time.time() - start_time))


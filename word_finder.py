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

def searcher(pos_words, end):
    futures = {}
    for i in pos_words:
        futures[i] = [j for j in end if j[0] == i[1]+1]
    return futures

def pathfinder(startig, start, length):
    print(start)
    pos_final = []
    
    def recurse(starting, starts):
        next_pos = [i for i in starts if i[0] == starting[1]+1]
        print(next_pos)
        
        if len(next_pos) == 0:
            if starting[1] + 1 == length:
                print("done")
                print("final", pos_final)
                return pos_final
            else:
                print(str(starting)+ "from " + str(starts))
                starts.remove(starting)
                pos_final.clear()
                recurse(startig, starts)

        elif len(next_pos) >= 1:
            nexts = next_pos[0]
            pos_final.append(nexts)
            recurse(nexts, starts)
    print("one")
    recurse(startig, start)
    return [startig] + pos_final

print(pathfinder((0,0), [(0, 0), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (5, 6), (5, 7), (7, 9), (8, 9), (10, 13)], 14))

def word_joiner(word_dict, string):
    completed = False
    final = ""
    
    starts = sorted(list(word_dict.values()), key = lambda x: x[0]) 
    ends = sorted(list(word_dict.values()), key = lambda x: x[1])
    index = 0
    future= {}
    while not completed:
        
        
        pos_words = [i for i in starts if i[0] == index]
        next_pos = [i for i in starts if i[0] == index+1]
        
        # print(pos_words)
        # print(index)
        if len(pos_words) == 1:
            index += len(get_key(pos_words[0], word_dict))
            final += get_key(pos_words[0], word_dict)
        
        else: 
            print(pos_words)
            print(future)
            print("starts", starts)
            full = 0
            
            future = searcher(pos_words, ends)

            for i in future:
                print("checks for availablitiy")
                if len(future[i]) > 0:
                    print("available")
                    full += 1
                    available = i
                else:
                    print("Here")
                    # future = searcher(pos_words, ends)
                    # print(future)
                    
            if full == 1:
                print("checks for one")
                final += get_key(available, word_dict)
                print(final)
                # pos_words = [i for i in starts if i[0] == index]
                index += len(get_key(available, word_dict))
            else:
                print("not one")
                future = searcher(pos_words, ends)
                
                
                    





        if index >= len(string):
           return final  

           
        
# print(word_joiner(word_finder("iwanttoeatfood"), "iwanttoeatfood"))
print("--- %s seconds ---" % (time.time() - start_time))


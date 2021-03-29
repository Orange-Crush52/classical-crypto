import time
import dictionaryload

word_list = dictionaryload.load('2of4brif.txt')

start_time = time.time()
def word_finder(string):
    # finds all words within a string
    words = {}
    string.replace(" ", "")
    for i in word_list:
        if i in string:
            words[i]= (string.find(i), string.find(i)+len(i)-1)
    
    return words

def get_key(val, dict):
    # gets the key value from the value
    for key, value in dict.items():
         if val == value:
             return key



def pathfinder(startig, start, length):
    # gets the correct word and position of each word in the sentence 
    pos_final = []
    
    def recurse(starting, starts):
        next_pos = [i for i in starts if i[0] == starting[1]+1]
        print("recurse")
        if len(starts) == 0:
            print("none")
            return None
        if len(next_pos) == 0:
            if starting[1] + 1 == length:
                print("final")
                start = starts
                return pos_final

            else:
                print(str(starting) + " from " + str(starts))
                starts.remove(starting)
                startig = starts[0]
                pos_final.clear()
                recurse(startig, starts)

        elif len(next_pos) >= 1:
            print("continue")
            nexts = next_pos[0]
            pos_final.append(nexts)
            recurse(nexts, starts)
    recurse(startig, start)
    return [start[0]] + pos_final


def word_joiner(word_dict, string):
    # finds a start point and joins together the positions 
    starts = sorted(list(word_dict.values()), key = lambda x: x[0]) 
    
    words = pathfinder(starts[0], starts, len(string))

    return " ".join([get_key(i, word_dict) for i in words])

        
print(word_joiner(word_finder("inawanttoeatfood"), "inawanttoeatfood"))
print("--- %s seconds ---" % (time.time() - start_time))


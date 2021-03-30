import time
import dictionaryload
import re

word_list = dictionaryload.load('2of4brif.txt')

start_time = time.time()
def word_finder(string):
    # finds all words within a string
    words = {}
    # print(string)
    string.replace(" ", "")
    for i in word_list:
        if i in string:
            count= 0
            for w in re.finditer(i, string):

                # words[i]= (string.find(i), string.find(i)+len(i)-1)
                words[i+str(count)] = (w.start(), w.end()-1)
                count+=1
    
    return words

def get_key(val, dict):
    # gets the key value from the value
    for key, value in dict.items():
         if val == value:
             return key



def word_joiner(word_dict, string):
    # finds a start point and joins together the positions 
    starts = sorted(list(word_dict.values()), key = lambda x: x[0]) 
    # print("string",string)

    pos_final = []
    length = len(string)
    startig = starts[0]
    start = starts
    future = 0
    def recurse(starting, starts):
        next_pos = [i for i in starts if i[0] == starting[1]+1]
        print("recurse")
        if len(starts) == 0:
            
            return ""
        if len(next_pos) == 0:
            if starting[1] + 1 == length:
                print("final")
                
                return #[start[0]] + pos_final

            else:
                print(str((get_key(starting, word_dict)+ str(starting))) + " from " + str(dict(zip([get_key(i, word_dict) for i in starts], starts))))
                starts.remove(starting)
                startig = starts[0]
                pos_final.clear()
                recurse(startig, starts)

        elif len(next_pos) >= 1:
            print("continue")
            nexts = next_pos[0]
            pos_final.append(nexts)
            recurse(nexts, starts)
        # try:
        #     recurse(startig, start)
        # except IndexError:
        #     return ""
    
    
    words = recurse(startig, start)
    sentence = [start[0]] + pos_final
    print(words)
    
    return " ".join([get_key(i, word_dict) for i in sentence])

print(word_finder("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline"), "bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline")
# print(word_joiner(word_finder("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspenalldayinline"), "bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspenalldayinline"))
print("--- %s seconds ---" % (time.time() - start_time))

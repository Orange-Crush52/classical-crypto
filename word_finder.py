import time
import dictionaryload
import re

word_list = dictionaryload.load('2of4brif.txt')


def word_finder(string):
    # finds all words within a string
    words = {}
    # print(string)
    string.replace(" ", "")
    for i in word_list:
        if i in string:
            count= 0
            for w in re.finditer(i, string):
                words[i+str(count)] = (w.start(), w.end()-1)
                count+=1
    
    return words

def get_key(val, dict):
    # gets the key value from the value
    for key, value in dict.items():
         if val == value:
             return key







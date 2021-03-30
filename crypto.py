
import dictionaryload
import frequency
import time
import word_finder
import numpy as np
import math
import re
import inspect 



az = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z",
    -1: " "
}
az_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0,
    0: 0

}
abcs = 'abcdefghijklmnopqrstuvwxyz'
word_list = dictionaryload.load('2of4brif.txt')
mult_modular_inverse = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23,
                        19: 11, 21: 5, 23: 17, 25: 25}
word_frequency = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m",
                  "f", "g", "p", "y", "b", "q", "v", "k", "z", "j", "x", "y"]
digraphs = ["th", "er", "on", "an", "re", "he", "in", "ed", "nd", "ha", "at", "en", "es", "of", 
"or", "nt", "ea", "ti", "to", "ti", "to", "it", "st", "io", "le", "is", "ou", "ar", "as", "de", "rt","ve"]
trigraphs = ["the", "and", "tha", "ent", "ion", "tio", "for", "nde", "has", "nce", "edt", "tis",
"oft", "oft", "sth", "men"]


def add_converter(string, adder):
    string = string.lower()
    lst_of_nums = [abcs.find(letter) + 1 for letter in string]
    new_string = ""
    for i in lst_of_nums:
        if i == 0:
            new_string += " "
        else:
            adder = adder % 26
            i += adder
            i = i % 26
            new_string += az[i]

    return new_string


def mult_converter(string, multiplier):
    string = string.lower()
    if int(multiplier) % 2 == 0 or multiplier == 13:
        return "Please choose a new multiplier. No even numbers or numbers divisible by 13"
    lst_of_nums = [abcs.find(letter) + 1 for letter in string]
    new_string = ""
    for i in lst_of_nums:
        if i == 0:
            new_string += " "
        else:
            multiplier = multiplier % 26
            i *= multiplier
            i = i % 26
            new_string += az[i]
    # mult_inverse = mult_modular_inverse[multiplier]

    return new_string  # , mult_inverse


def affine_converter(string, multiplier, adder):
    string = mult_converter(string, multiplier)
    string = add_converter(string, adder)
    return string


def add_solver(string):
    lst_of_p = []
    possibilities = []
    actuall = ""
    string = string.lower()
    string = string.split(" ")

    for i in string:
        x = 0
        # print(i)
        if string in word_list:
            possibilities.append(string)
        else:
            for count in range(1, 27):
                count = count % 26
                poss = add_converter(i, count)

                if poss in word_list:
                    x += 1
                    possibilities.append(poss)
                    possibilities.append(count)
                    az_count[count] += 1
                    if not count in lst_of_p:
                        lst_of_p.append(count)

                    # print(x)
        if x == 0:

            guess = "guess: "
            for w in lst_of_p:
                guess += add_converter(i, w) + " " + str(w) + ", "
            possibilities.append(guess)
    maxed = 0
    for i in az_count:
        if az_count[i] > maxed:
            maxed = list(az_count.keys())[i - 1]
    for i in string:
        actuall += add_converter(i, maxed) + " "

    return possibilities, maxed, actuall


def mult_solver(string):
    lst_of_p = []
    possibilities = []
    actuall = ""
    string = string.lower()
    string = string.split(" ")

    for i in string:
        x = 0
        # print(i)
        if string in word_list:
            possibilities.append(string)
        else:
            for count in mult_modular_inverse.values():
                poss = mult_converter(i, count)
                # i is the word not the letter
                if poss in word_list:
                    x += 1
                    possibilities.append(poss)
                    possibilities.append(count)
                    az_count[count] += 1
                    if not count in lst_of_p:
                        lst_of_p.append(count)

        if x == 0:

            guess = "guess: "
            for w in lst_of_p:
                guess += mult_converter(i, w) + " " + str(w) + ", "
            possibilities.append(guess)

    maxed = 0
    for i in az_count:
        # print(az_count[i])
        # print(maxed)
        if az_count[i] > maxed:
            maxed = list(az_count.keys())[i - 1]
    for i in string:
        actuall += mult_converter(i, maxed) + " "

    return possibilities, maxed, actuall


def affine_solver(string, priority):
    # solves codes made by an affine cypher

    string = string.lower()

    a_possibilities = mult_modular_inverse.keys()
    string_freq_list = frequency.order(frequency.frequency(string))

    # most common letter is e or in numbers 5 you can assume string_freq_list[0] is e 
    possibilities = []
    for i in string_freq_list:
        for j in a_possibilities:
            for b in range(26):
                if i == j + b:
                    pose = affine_converter(string, j, b).split(" ")
                    if len([i for i in pose if i in word_list]) > len(pose)/2:
                        possibilities.append((pose, "adder: ", b, "multiplier: ", j))
                        if priority:
                            return possibilities
    return possibilities

def inverse_determanint(matrix, determinant=None):
    # print(mult_modular_inverse(determinant))
    if determinant != None:
        new = np.array([[matrix[1][1], -matrix[0][1]],[-matrix[1][0], matrix[0][0]]])

        mult_inverse = (new.dot(mult_modular_inverse[determinant])) % 26


    else:
        determanint = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26
        new = np.array([[matrix[1][1], -matrix[0][1]],[-matrix[1][0], matrix[0][0]]])

        # print(determanint)
        mult_inverse = (new.dot(mult_modular_inverse[determanint])) % 26

    return mult_inverse

# print(inverse_determanint(np.array([[4, 5], [3, 6]])))

def hill_converter(string, matrix, grouping):
    # converts string to hill cypher using matrix
    # print(matrix)
    string = string.lower()
    try: 
        determanint = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26
    except:
        return
    # deternment checker
    
    # print(determanint)
    if determanint == 13:
        return "matrix determinants(ad-bc) can't be a multiple of 13"
    if (inverse_determanint(matrix)[0][0]*inverse_determanint(matrix)[1][1] - inverse_determanint(matrix)[0][1]*inverse_determanint(matrix)[1][0]) % 26 == 13:
        return "cypher is not able to be solved"
    if determanint % 2 == 0:
        return "matrix determinants(ad-bc) can't be an even number"
    if ((inverse_determanint(matrix)[0][0]*inverse_determanint(matrix)[1][1] - inverse_determanint(matrix)[0][1]*inverse_determanint(matrix)[1][0]) % 26) % 2== 0:
        return "matrix is not able to be solved"
    inverse_key = inverse_determanint(matrix, determanint)

    string_spaces = string.split(" ")
    # string.replace(" ", "")
    if len(string) % 2 != 0:
        string += "x"
    # Breaks the strings into groups of grouping 
    out = [(string[i:i+grouping]) for i in range(0, len(string), grouping)] 
    # -1 is space
    final =""
    for group in out:
        # transfers the string to the number froms than places them into a numpy array 
        numbers = np.array(list(map(lambda i: abcs.find(i)+1, group))).reshape(1, 2)#.tolist()
        # flattens lists
        flatten = lambda l: [item for sublist in l for item in sublist]
        # this is where the numbers are encoded using the matrix
        mult_matrix = np.array(list(map(lambda j: (matrix.dot(j)) % 26, numbers)))
        # converts the numbers back to string and than puts it into final
        final += "".join(list(map(lambda i: az[i-1], flatten(mult_matrix))))

    pos = 0
    words = list(final)
    for i in range(len(string_spaces)):
        words.insert(pos+i, " ")
        pos += len(string_spaces[i])
    
    return "".join(words).strip(" ") , inverse_key

# print(hill_converter("clds", np.array([[16, 7], [17, 23]]), 2))

def dert_checker(matrix):
    determanint = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26
    if determanint == 13:
        return False
    elif determanint % 2 == 0:
        return False
    else:
        return True
    



start_time = time.time()
# print(mult_converter("hello my name is connor", 15))
# print(add_converter("ucffng", 23))
# print(affine_converter("hello my name is connor would you like to buy an orange shirt ", 3, 19))
# print(add_solver("Zit Zqkutz Ol Qlwgk Vig Iql Zit Wtlz Vggr Exzzofu Dqeioftl"))
# print(mult_solver("pwxxq mk bomw ey sqbbqj"))
# the number we are using will always be one less than the one in the paper since our a starts at 0
# print(affine_solver("qhccl fp ivfh tx bliilu jldce pld ctzh al ydp vi luvinh xqtua ", True))
# print(hill_converter("iwanttoeatfood", np.array([[5, 3],[11, 8]]), 2))
# print(inverse_determanint(np.array([[4, 5],[3, 6]]), 9))


print("--- %s seconds ---" % (time.time() - start_time))

# 15, 12, 1, 25
# remember to change the message back to only one e for each time

# the letter frequency = plaintext




# if the inverse deternamint of the first two is even or 13 than it also doesn't work





def tester(string):
    a_solve = add_solver(string)
    m_solve = mult_solver(string)
    return a_solve, m_solve

# tester()

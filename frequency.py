

rang = range(26)


def frequency(string):
    string = string.replace(" ", "")
    string = string.lower()
    abcs = 'abcdefghijklmnopqrstuvwxyz'
    string = [abcs.find(letter) + 1 for letter in string]
    count = {
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
    for i in rang:
        if i in string:
            num = string.count(i)
            count[i] += num
        else:
            count[i] = -1
    return count





def order(letter_count):
    # 5, 20, 1, 15, 9, 14, 19, 8, 18, 4, 12, 3, 21, 13, 6, 7, 16, 25, 2, 17, 22, 11, 26, 10, 24, 25
    none = []
    # for i in rang:
    #     if letter_count[i] == -1:
    #         value = letter_count.pop(i)
    #         none.append(i)
    most_list = []
    found = []
    for i in letter_count.keys():
        most = 0
        letter = 0

        for w in letter_count.keys():
            if letter_count[w] > most:

                if not w in found:
                    most = letter_count[w]

                    letter = w
        found.append(letter)
        most_list.append(letter)

    final = most_list + none

    return final


# print(order(frequency("hello my name is connor")))


def group_letter_count(string):
    string = string.lower()
    found = []
    frequencies = {}
    for i in range(len(string)):
        group = string[i]+string[i+1]
        
        if group in found:
            frequencies[group]+=1
        else:
            found.append(group)
            frequencies[group] = 1

    return frequencies

    
print(group_letter_count("hEllo my nameme is jack"))
# print(order(group_letter_count("hEllllo my nameme is connorhe")))


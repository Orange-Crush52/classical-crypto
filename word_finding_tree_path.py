import word_finder

word_dict = word_finder.word_finder("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline")




def get_key(val, dict):
    # gets the key value from the value
    for key, value in dict.items():
         if val == value:
             return key



lsts = {}

class Inter():
    # Makes sure there no repeat values across seperate lists
    def __init__(self, items):
        global lsts 
        self.self = self
        self.items = items

        lsts[self] = self.items

    def add(self, item):
        lsts[self].append(item)
        for i in lsts:
            if item in i.items:
                self.items.append(i.items.pop(i.items.index(item)))
                
        self.items.append(item)
        self.indup()

    def indup(self):
        singles = []
        self.items = [singles.append(i) for i in self.items if i not in singles]
        self.items = singles



class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def parent(self,pos, tree):

        return [i for i in tree if i[1]+1 == pos.data[0]]  

    def branch_cutter(self, branch, branchess):
        # branch is the begining of the list being removed
        # branches is all of the tree objects
        more = True

        while more:

            del branchess[get_key(branch, branchess)]
            parents = self.parent(branch, branchess)
                
            for parent in parents:
                branchess[parent].children.remove(branch)

            if len(branch.children) > 0:
                branch = branch.children[0]

            else:
                more = False
                
        return branchess


def tree_grower(words, length):
    # takes length of all words found and length of originol string and return a string with spaces in the 
    # correct places
    global branches, split, straight, pos_finals
    searche = sorted(list(words.values()), key = lambda x: x[1])
    next_pos = lambda lengths, point : [length for length in lengths if length[0] == point[1]+1]
    branches = {j:Tree(j) for j in searche}
    for i in branches:
        branches[i].children = [branches[j] for j in next_pos(searche, i)]

    pos_finals = []
    
    #split is a list of all values that have more than one child under them
    split = Inter([branches[list(branches.keys())[0]]])
    # straight is a list of values that only have one child under them
    straight = Inter([])
    root = list(branches.keys())[0]

    def tree_trimmer(current):
 
        global branches, split, straight, pos_finals


    #     try:
    #         # print("split", [get_key(j, word_dict) for j in [i.data for i in split.items]] , "straight",[get_key(j, word_dict) for j in [i.data for i in straight.items]], "current", get_key(current.data, word_dict))
    #         # print(get_key(current.data, word_dict), [get_key(i, word_dict) for i in [j.data for j in current.children]])
    # except AttributeError:
    #         print("split", [get_key(j, word_dict) for j in [i.data for i in split.items]] , "current", get_key(current.data, word_dict), "straight", straight.items)
        if len(current.children) >1:
            split.add(current)

            # tree_trimmer(sorted(current.children,key=lambda x: len(get_key(x.data, word_dict)),reverse=True)[0])
            tree_trimmer(current.children[0])

        elif len(current.children) == 1:
            straight.add(current)
            
            # tree_trimmer(sorted(current.children,key=lambda x: len(get_key(x.data, word_dict)),reverse=True)[0])
            tree_trimmer(current.children[0])

        else:

            if current.data[1]+1 == length:
                # sorted(list(word_dict.values()), key = lambda x: x[0])
                pos_finals = sorted(list([i.data for i in split.items]) + list([i.data for i in straight.items]) + [current.data], key = lambda x:x[1])
                
                

            else:
                # the lst is a Inter object
                # gets the last item from an Inter object 
                cut = lambda lst: sorted(lst.items, key=lambda x: x.data[1])[-1]
                # far is any values that are too far ahead
                far = [i for i in straight.items if i.data[0] >= cut(split).data[1]]
                for i in far:
                    straight.items.remove(i)
                branches = current.branch_cutter(current, branches)

                tree_trimmer(cut(split))
    
    tree_trimmer(branches[root])
    
    return " ".join([get_key(i, word_dict)[:-1] for i in pos_finals])


print(tree_grower(word_dict, 110))
# print(len("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline"), "bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline")






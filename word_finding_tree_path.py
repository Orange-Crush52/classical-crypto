from typing import List
import word_finder

word_dict = word_finder.word_finder("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline")

starts = sorted(list(word_dict.values()), key = lambda x: x[0])
# print(starts)

next_pos = lambda lengths, point : [length for length in lengths if length[0] == point[1]+1]


def get_key(val, dict):
    # gets the key value from the value
    for key, value in dict.items():
         if val == value:
             return key



lsts = {}

class Inter():
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
        # print("parents", [i for i in tree if i[1]+1 == pos.data[0]] )
        return [i for i in tree if i[1]+1 == pos.data[0]]  

    def branch_cutter(self, branch, branchess):
        # branch is the begining of the list being removed
        # branches is all of the tree objects
        more = True
        while more:
            # print("more", more)
            # print(branch)
            del branchess[get_key(branch, branchess)]
            if len(branch.children) > 0:
                branch = branch.children[0]
                # print(branch.data)
                # print("if")
            else:
                # print("else")
                # can occasionaly have more than one parent
                parents = self.parent(branch, branchess)
                
                for parent in parents:
                    branchess[parent].children.remove(branch)
                more = False
                
        return branchess



def tree_grower(searche, length):
    global branches, split, straight, pos_finals

    branches = {j:Tree(j) for j in searche}
    # print(branches)
    for i in branches:
        # print(i)
        branches[i].children = [branches[j] for j in next_pos(searche, i)]

    pos_finals = []
    
    split = Inter([branches[list(branches.keys())[0]]])
    straight = Inter([])
    root = list(branches.keys())[0]
    def tree_trimmer(current):
    
        global branches, split, straight, pos_finals
        # try:
        # print("split", [i.data for i in split.items] , "straight", [i.data for i in straight.items], "current", current.data)
        # except AttributeError:
        #     print("split", [i.data for i in split.items] , "current", current.data, "straight", straight.items)
        if len(current.children) >1:
            # print(current in branches, current.data, current)
            # print(str(current.data) + " is a split")
            split.add(current)
            
            # print("more than one")
            tree_trimmer(current.children[0])
        
        elif len(current.children) == 1:
            # print(str(current.data) + " is a straight")
            # print("one")
            straight.add(current)

            tree_trimmer(current.children[0])
        

        else:
            # print(current in branches, current.data, current)
            if current.data[1]+1 == length:
                # print("end")
                # sorted(list(word_dict.values()), key = lambda x: x[0])
                final_string = ""
                pos_finals = sorted(list([i.data for i in split.items]) + list([i.data for i in straight.items]) + [current.data], key = lambda x:x[1])
                
                return

            else:
                # print("children of current is none")
                # print("straight", straight)
                # print("potential straight", current.data)
                # the lst is a Inter object
                cut = lambda lst: sorted(lst.items, key=lambda x: x.data[1])[-1]
                try:
                    # print("try")
                    # print("cut",cut(straight).data)
                    # branches = cut(straight).branch_cutter(cut(straight), branches)
                    branches = current.branch_cutter(current, branches)
                    # print("try success")
                except (IndexError, AttributeError):
                    # print("except")
                    
                    branches = current.branch_cutter(current, branches)
                    
                tree_trimmer(cut(split))
    
    tree_trimmer(branches[root])
    
    return " ".join([get_key(i, word_dict)[:-1] for i in pos_finals])

print(word_dict)
print(tree_grower(starts, 110))

# print(len("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline"), "bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspendalldayinline")





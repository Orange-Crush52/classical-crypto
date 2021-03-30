from typing import List
import word_finder

word_dict = word_finder.word_finder("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspenalldayinline")

starts = sorted(list(word_dict.values()), key = lambda x: x[0])

# would find all the children of the node 
# next_pos = [i for i in starts if i[0] == starting[1]+1]

next_pos = lambda lengths, point : [length for length in lengths if length[0] == point[1]+1]


def get_key(val, dict):
    # gets the key value from the value
    for key, value in dict.items():
         if val == value:
             return key



lsts = []

class Inter():
    def __init__(self, items):
        global lsts 
        self.self = self
        self.items = items

        lsts.append(self.items)

    def add(self, item):
        for i in lsts:
            if item in i:
                self.items.append(i.pop(i.index(item)))
                
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
        print("parents", [i for i in tree if i[1]+1 == pos.data[0]] )
        return [i for i in tree if i[1]+1 == pos.data[0]]  

    def branch_cutter(self, branch, branchess):
        # branch is the begining of the list being removed
        # branches is all of the tree objects
        print(branch.data, " from ", [i.data for i in list(branchess.values())])
        # print(branch, " from ", branchess)
        more = True
        while more:
            print("more", more)
            print(branch)
            del branchess[get_key(branch, branchess)]
            if len(branch.children) > 0:
                branch = branch.children[0]
                print(branch.data)
                print("if")
            else:
                print("else")
                # can occasionaly have more than one parent
                parents = self.parent(branch, branchess)
                
                for parent in parents:
                    branchess[parent].children.remove(branch)
                more = False
                
        return branchess

    def leaves(self, tree):
        # leaves is the data
        return 



def tree_grower(searche, length):
    global branches, split, straight

    branches = {j:Tree(j) for j in searche}
    # print(branches)
    for i in branches:
        # print(i)
        branches[i].children = [branches[j] for j in next_pos(searche, i)]

    pos_final = []
    
    split = {branches[list(branches.keys())[0]]}
    straight = set()
    root = list(branches.keys())[0]
    def tree_trimmer(current):
    
        global branches, split, straight
        try:
            print("split", split , "straight", straight, "current", current.data)
        except AttributeError:
            print("split", split, "current", current.data, "straight", straight)
        if len(current.children) >1:
            # print(current in branches, current.data, current)
            print(str(current.data) + " is a split")
            split.add(current)
            
            print("more than one")
            tree_trimmer(current.children[0])
        
        elif len(current.children) == 1:
            print(str(current.data) + " is a straight")
            print("one")
            straight.add(current)

            tree_trimmer(current.children[0])
        

        else:
            # print(current in branches, current.data, current)
            if current.data[1]+1 == length:
                # needs better end checking functionality
                # should add all of the lengths 
                print("end")
                return branches

            else:
                print("children of current is none")
                # print("straight", straight)
                # print("potential straight", current.data)
                # might have to change to x[0] right now its sorting by end point
                cut = lambda lst: sorted(list(lst), key=lambda x: x.data[1])[-1]
                try:
                    print("try")
                    branches = cut(straight).branch_cutter(cut(straight), branches)
                    print("try success")
                except (IndexError, AttributeError):
                    print("except")
                    
                    branches = current.branch_cutter(current, branches)
                    
                    print("except success")
                tree_trimmer(cut(split))
    # print(branches[root])
    return tree_trimmer(branches[root])

# It might be going to far make sure to allow it to go backwards 

tree_grower(starts, 109)

# print(len("bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspenalldayinline"), "bobwantstogotogreatadventuretomorrowbutiwouldrathergototheshoreifwegototheamusementparkwewillspenalldayinline")



"""
# a binary tree will only have 2 subbranches (binary=two)
# every node only has 2 subbranches.
# every parent node will only split off into two child nodes max. the cycle can repeat.
# TREE TRAVERSAL: the path in which we can visit each node. you always start from leaf nodes.
# there are THREE main ways:
# 1. pre-order traversal: start with the root (original) node, then go to the left, then the right, working down.
# 2. post-order traversal: with a left, right, root, pattern, start with start from the leaves, then go to the parent of the leaves
# then go to the neighbouring subtree, and keep going up until you reach the main root. 
# 3. in-order traversal: left, root, right, starting from a sub tree, then following branches up to the root, then following the branch to the next subtree.
"""

class Treenode:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None 

def inOrder(root):
    if root.leftnode != None:
        inOrder(root.leftnode)

    print(root.data)
    if root.rightnode!=None:
        inOrder(root.rightnode)

def preOrder(root):
    print(root.data)
    if root.leftnode != None:
        preOrder(root.leftnode)

    if root.rightnode !=None:
        preOrder(root.rightnode)
    
def postOrder(root):
    if root.leftnode != None:
        postOrder(root.leftnode)
        
    if root.rightnode != None:
        postOrder(root.rightnode)

    print(root.data)



treeone=Treenode(5)

treeone.leftnode=Treenode(4)
treeone.rightnode=Treenode(2)

treeone.leftnode=Treenode(7)

treeone.rightnode=Treenode(8)

"""

treeone.rightnode=Treenode(9)
"""

inOrder(treeone)
print()
preOrder(treeone)
print()
postOrder(treeone)







        


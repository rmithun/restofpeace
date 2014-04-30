###Binary search tree class

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
       if root.data > node.data:
       #if root.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
       else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

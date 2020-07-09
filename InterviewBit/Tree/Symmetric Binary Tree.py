class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.val  = key


def invert(root):

    if root is None:
        return 

    temp = root

    invert(temp.left)
    invert(temp.right)

    temp.left , temp.right = temp.right , temp.left

def inOrder(root):

    node_list = []

    helper(root,node_list)

    return node_list

def helper(root,node_list):

    if root:

        if root.left != None:
            helper(root.left,node_list)

        node_list.append(root.val)

        if root.right != None:
            helper(root.right,node_list)

def symmetric(A):

    tree_list = inOrder(A)

    invert(A)

    tree_rev_list = inOrder(A)

    print(tree_list[0],tree_rev_list)

    if(tree_list == tree_rev_list):
        return 1
    else:
        return 0

   

root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3) 


print(symmetric(root))
    

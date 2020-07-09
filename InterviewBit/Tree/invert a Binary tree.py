class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.val  = key

def invert(root):

    if root is None:
        return 0

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

root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3) 

print("Inorder traversal of the constructed tree is")  
print(inOrder(root))  
      
""" Convert tree to its mirror """
invert(root)  

print("\nInorder traversal of the mirror treeis ")
print(inOrder(root))  

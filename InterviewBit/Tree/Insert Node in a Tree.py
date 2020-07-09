class TreeNode: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 

# Function to insert node in tree recursively
def insertNode(root,node): 
    if root is None: 
        root = node 

    else: 

        if root.data < node.data: 
            if root.right is None: 
                root.right = node 
            else: 
                insertNode(root.right, node) 

        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insertNode(root.left, node) 

def inOrder(root,tree):

    tree = []
  
    if root: 
  
        # First recur on left child 
        inOrder(root.left,tree) 
  
        # then print the data of node 
        tree.append(root.data) 
  
        # now recur on right child 
        inOrder(root.right,tree)

    return tree
        

def postOrder(root):

    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)

def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

r = TreeNode(3)

insertNode(r,TreeNode(2))
insertNode(r,TreeNode(4))


# Print inoder traversal of the BST 
print(inOrder(r,list()))

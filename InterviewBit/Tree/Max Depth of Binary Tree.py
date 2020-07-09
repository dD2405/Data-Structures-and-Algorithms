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

def maxDepth(root):
    if root is None:
        return 0
  
    else:
        left = maxDepth(root.left) 
        right = maxDepth(root.right) 
  
        if (left > right):
            return left+1
        else: 
            return right+1

r = TreeNode(3)

insertNode(r,TreeNode(2))
insertNode(r,TreeNode(5))
insertNode(r,TreeNode(4))
print(maxDepth(r))

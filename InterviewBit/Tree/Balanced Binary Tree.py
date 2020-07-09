class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.val  = key

def maxDepth_left(root):
    if root is None:
        return 0
  
    else:
        left = maxDepth_left(root.left) 
        return left+1

def maxDepth_right(root):
    if root is None:
        return 0
  
    else:
        right = maxDepth_right(root.right) 
        return right+1

def balance(A):

    result = maxDepth_left(A) - maxDepth_right(A)

    if(result <= 1):
        return 1
    else:
        return 0


    
root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3)
root.left.left.left = Node(7) 
#root.left.right = Node(4)
#root.right.left = Node(4)
#root.right.right = Node(3) 

print(balance(root))

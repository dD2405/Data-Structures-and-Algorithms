class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.val  = key

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

def isValidBST(root):
    result = inOrder(root)
    print(result)

    if(result == sorted(result)):
        if(result[0] == result[1]):
            return False
        else:
            return True
    else:
        return False

root = Node(2) 
root.left = Node(1) 
root.right = Node(3)

print(isValidBST(root))

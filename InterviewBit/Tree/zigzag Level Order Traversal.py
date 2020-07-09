class Node: 
    # A utility function to create a new node 
    def __init__(self ,key): 
        self.data = key 
        self.left = None
        self.right = None
  
# Iterative Method to print the height of binary tree 
def zigzag(root): 
    # Base Case 
    if root is None: 
        return
      
    # Create an empty queue for level order traversal 
    queue,result,level = [],[], 1
  
    # Enqueue Root and initialize height 
    queue.append(root) 
  
    while(len(queue) > 0): 
        # Print front of queue and remove it from queue 
        result.append(queue[0].data)

        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
  
        if node.right is not None:
            queue.append(node.right)
            

    return result
  
#Driver Program to test above function 
root = Node(3) 
root.left = Node(9) 
root.right = Node(20)
root.left.right = Node(10)
root.left.left = Node(11)
root.right.left = Node(15) 
root.right.right = Node(7) 
  
print(zigzag(root))

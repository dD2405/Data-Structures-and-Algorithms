class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.data = key

def insert(root,node):

    if root is None:
        root = node

    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)

        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)


def preOrder(root):

    if root is None:
        return 

    current = root
    stack,res=[],[]

    stack.append(current)

    while(len(stack)>0):
        node = stack.pop()
        res.append(node.data)

        if node.right is not None:
            stack.append(current.right)

        if node.left is not None:
            stack.append(current.left)

    return res


r = Node(3)

insert(r,Node(2))
insert(r,Node(4))

print(preOrder(r))

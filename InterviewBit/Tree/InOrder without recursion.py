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

def inOrder(root):

    current = root
    stack,res = [],[]

    while(True):
        if current is not None:
            stack.append(current)
            current = current.left
            print(stack)

        elif(stack):
            current = stack.pop()
            res.append(current.data)

            print('answer:',res)
            current = current.right
            print('right:',current)

        else:
            break

    return res

r = Node(3)

insert(r,Node(2))
insert(r,Node(4))

print(inOrder(r))

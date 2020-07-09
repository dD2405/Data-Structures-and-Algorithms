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


def minDepth(A):

    if A is None:
        return 0

    elif A.left is None and A.right is None:
        return 1

    elif A.left is None:
        return minDepth(A.right)+1

    elif A.right is None:
        return minDepth(A.left)+1

    else:
        return min(minDepth(A.left),minDepth(A.right))+1
        

r = Node(7)

insert(r,Node(2))
insert(r,Node(4))
insert(r,Node(5))
insert(r,Node(3))
insert(r,Node(1))
insert(r,Node(8))
insert(r,Node(9))
insert(r,Node(10))

print(minDepth(r))

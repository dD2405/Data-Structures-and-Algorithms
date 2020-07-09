class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.data = key

def insert_1(root1,node):

    if root1 is None:
        root = node

    else:
        if root1.data < node.data:
            if root1.right is None:
                root1.right = node
            else:
                insert_1(root1.right,node)

        else:
            if root1.left is None:
                root1.left = node
            else:
                insert_1(root1.left,node)

def insert_2(root2,node):

    if root2 is None:
        root2 = node

    else:
        if root2.data < node.data:
            if root2.right is None:
                root2.right = node
            else:
                insert_2(root2.right,node)

        else:
            if root2.left is None:
                root2.left = node
            else:
                insert_2(root2.left,node)

def inOrder(root):

    result = []

    helper(root,result)
    return result

def helper(root,result):

    if root:
        if root.left != None:
            helper(root.left,result)

        result.append(root.data)

        if root.right != None:
            helper(root.right,result)

def check(r1,r2):

    if(inOrder(r1) == inOrder(r2)):
        return 1
    else:
        return 0
        

r1 = Node(5)

insert_1(r1,Node(2))
insert_1(r1,Node(4))

r2 = Node(5)

insert_2(r2,Node(6))
insert_2(r2,Node(4))

print(check(r1,r2))


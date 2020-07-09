class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.val  = key

def insert(root,new_node):

    if root is None:
        return None

    else:
        if root.val < new_node.val:

            if root.right is None:
                root.right = new_node
            else:
                insert(root.right,new_node)

        else:
            if root.left is None:
                root.left = new_node
            else:
                insert(root.left,new_node)

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


def kth_smallest(root,k):

    result = inOrder(root)

    print(result)

    return result[k-1]


r = Node(5)

insert(r,Node(4))
insert(r,Node(3))
insert(r,Node(6))
insert(r,Node(7))

k = 2

print(kth_smallest(r,k))
            

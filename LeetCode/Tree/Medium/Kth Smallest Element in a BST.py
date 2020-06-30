# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = self.inOrder(root)
        return result[k-1]
    
    def inOrder(self,A):
        node_list = []

        self.helper(A,node_list)

        return node_list

    def helper(self,A,node_list):
        if A:
            if A.left != None:
                self.helper(A.left,node_list)

            node_list.append(A.val)

            if A.right != None:
                self.helper(A.right,node_list)
        

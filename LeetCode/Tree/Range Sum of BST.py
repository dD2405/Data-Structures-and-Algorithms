# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inOrder(self,root):
        node_list = []
        
        self.helper(root,node_list)
        
        return node_list 
    
    def helper(self,root,node_list):
        if root:
            if root.left != None:
                self.helper(root.left,node_list)
            
            node_list.append(root.val)
            
            if root.right != None:
                self.helper(root.right,node_list)
                
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        result = self.inOrder(root)
        
        output = 0
        
        for ele in result:
            if(L < ele  < R):
                output = output + ele
        
        output = output + L + R
        
        
        return output

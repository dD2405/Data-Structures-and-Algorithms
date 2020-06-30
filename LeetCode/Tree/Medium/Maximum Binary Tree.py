# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
     def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def maxTree(nums):
            idx=nums.index(max(nums))
            node = TreeNode(nums[idx])
            
            if len(nums[idx+1:]) > 0:
                node.right = maxTree(nums[idx+1:])
            
            if len(nums[:idx]) > 0:
                node.left = maxTree(nums[:idx])
            
            return node
        
        return maxTree(nums)
        

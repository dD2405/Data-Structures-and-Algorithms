'''Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.  '''

class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        local_max = 0
        global_max = -200000000000000000000000000000000000000000
        
        for i in range(len(A)):
            local_max = max(A[i],(A[i] + local_max))
            if(local_max > global_max):
                global_max = local_max
        return global_max
        

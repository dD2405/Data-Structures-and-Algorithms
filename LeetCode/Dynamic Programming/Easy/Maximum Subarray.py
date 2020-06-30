class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        local_max = 0
        global_max = -200000000000000000000000000000000000000000
        
        for i in range(len(A)):
            local_max = max(A[i],(A[i] + local_max))
            if(local_max > global_max):
                global_max = local_max
        return global_max
        

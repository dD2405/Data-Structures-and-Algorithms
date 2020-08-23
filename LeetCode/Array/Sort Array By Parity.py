''' Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted. '''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd, even = [], []
        
        for ele in A:
            if ele % 2 == 0:
                even.append(ele)
            else:
                odd.append(ele)
        
        return even + odd
        
        

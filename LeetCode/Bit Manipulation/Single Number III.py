''' Given an array of numbers nums, in which exactly two elements appear 
only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?  '''


# Using collections.Counter()

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]):
        
        res = Counter(nums).most_common()[:-3:-1]
        ans = [element[0] for element in res]
        return ans 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*************************************************************************************************************************************************************************
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using set() difference properties 
# Where set(A) - set(B) = All elements present in A but not in B

class Solution(object):
    def singleNumber(self, nums: List[int]) -> List[int]):
        one = set()
        double = set()
        for n in nums:
            if n not in one:
                one.add(n)
            else:
                double.add(n)
                
        return list(one - double)

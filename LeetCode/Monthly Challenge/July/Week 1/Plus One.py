'''Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(nums) for nums in digits]
        number_str = ''.join(digits)
        number_int = int(number_str)
        result_int = number_int + 1
        
        result_str = str(result_int)
        result = list(result_str)
        final_result = [int(ele) for ele in result]
        
        return final_result
        

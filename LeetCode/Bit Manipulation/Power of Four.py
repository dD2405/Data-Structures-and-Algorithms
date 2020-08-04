''' Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?  '''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        num = format(num, '0b')
        count_zeros = len(num) - len(num.rstrip('0'))
        count_ones = num.count('1')
        
        if count_zeros % 2 == 0 and num[0] == '1' and count_ones == 1 :
            return True
        
        else:
            return False
        

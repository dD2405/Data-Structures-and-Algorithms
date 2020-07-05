''' Given a 32-bit signed integer, reverse digits of an integer.

Sample:
Input: 123
Output: 321

Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.'''

class Solution:
    def reverse(self, number: int) -> int:
        if number > 2**31-1 or number < -2**31:
            return 0
        else:
            if(number>0):
                number=str(number)
                reverse=number[::-1]
            else:
                number = number * -1
                number=str(number)
                number=number[::-1]
                reverse='-'+number

        reverse=int(reverse)
        
        if int(reverse) >= 2**31-1 or int(reverse) <= -2**31:
            return 0
        else:
            return reverse 

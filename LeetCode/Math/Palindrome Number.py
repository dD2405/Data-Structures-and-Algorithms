''' Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1'''
-----------------------------------------------------------------------------------------------

SOLUTION 1 :- 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        a = str(x)
        
        li = list(a)

        li_rev = li[::-1]

        print(li_rev)

        res = ''.join(li_rev)

        if a == res:
            return True
    
        else:
            return False
            
SOLUTION 2:-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        
        a = x[::-1]

        if a == x:
            return True
    
        else:
            return False
        

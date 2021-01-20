''' Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true  '''

-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                current_char = stack.pop()
                
                if current_char == '(':
                    if char != ')':
                        return False
                if current_char == '{':
                    if char != '}':
                        return False
                
                if current_char == '[':
                    if char != ']':
                        return False
        if stack:
            return False
        
        return True
        

'''The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231. 

 EXAMPLE
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.'''


class Solution:
    def hammingDistance(self, n1: int, n2: int) -> int:
        
        # XOR Operation
        x = n1 ^ n2  
        setBits = 0
  
        while (x > 0): 
            # AND Operation
            setBits += x & 1
            
            # Bitwise shifting by 1
            x >>= 1
      
        return setBits  
        

''' You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

    1 <= n <= 45 '''

# Fibonacci Sequence
class Solution:
    def climbStairs(self, n: int) -> int:
        
        n1,n2 = 0,1
        
        for i in range(n):
            res = n1+n2
            n1,n2 = n2,res
        
        return res

------------------------------------------------------------------------------------------------------------------------------------------------------------
***********************************************************************************************************************************************************
------------------------------------------------------------------------------------------------------------------------------------------------------------

# Recursion With Memoization (Dynamic Wtih recursion)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        return self.helper(0,n,memo)
        
    def helper(self, i, n, memo):
        if i > n:
            return 0

        if i == n:
            return 1

        if memo[i] > 0:
            return memo[i]

        memo[i] = self.helper(i+1, n, memo) + self.helper(i+2, n, memo)
        return memo[i]

--------------------------------------------------------------------------------------------------------------------------------------------------------------
**************************************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------------------------------
        
# Dynamic Programming without recursion

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        if n == 2 or n == 3:
            return n
        
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n+1):
            dp[i]  = dp[i-1] + dp[i-2]

        return dp[n]
        

        

        
        


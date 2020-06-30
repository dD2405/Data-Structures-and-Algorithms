def climbStairs(A):
    n1,n2 = 0,1
        
    for i in range(A):
        res = n1+n2
        n1,n2 = n2,res
        
    return res

print(climbStairs(7))

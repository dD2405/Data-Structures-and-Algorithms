class Node:

    def __init__(self,data):
        self.val = data
        self.next = None

class Solution:

    def mergeNode(self,A,B):
        m = self.NodeLength(A)
        n = self.NodeLength(B)
        d = n-m

        if(m>n):
            A,B = B,A
            d = m-n

        for i in range(d):
            B = B.next

        while(A != None and B != None):
            if A==B:
                return A
            A = A.next
            B = B.next
        return None

    def NodeLength(self,a):
        n = a
        i = 0

        while(n != None):
            n = n.next
            i += 1
        return i



from math import gcd

def cpFact(A, B):
    for x in range(2,A):
        if(A%x==0 and gcd(B,x)==1):
            return x
            break


print(cpFact(30,12))

import time

start = time.time()

def stnum(m):
    d=m//2
    s=0
    for i in range(1,d+1):
        if(m%i==0):
            s=s+i

    return s

s2=0
for j in range(200,10000):
    a=stnum(j)
    b=stnum(a)
    if(b==j and a>j):
        s2=s2+j+a

end  = time.time() - start
print("time taken-",end)
print (s2)

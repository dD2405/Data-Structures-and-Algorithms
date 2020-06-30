import time
start = time.time()
large = 0
num=0

def check(j):
    c=0
    while(j!=1):
        if(j%2==0):
            j=j/2
        else:
            j=3*j+1
        c+=1
    return c

for i in range(1,1000000):
    x=check(i)
    if(x>large):
        large=x
        num=i

print (num)
print (large)
end  = time.time() - start

print(end)
    

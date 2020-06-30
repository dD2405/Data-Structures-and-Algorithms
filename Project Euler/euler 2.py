import time
start = time.time()
s,c=0,0
a,b=0,1

while c<=4000000:
    if(c%2==0):
        s=s+c
    c=a+b
    a=b
    b=c
       
        
end = time.time() - start
print (s)
print(end)

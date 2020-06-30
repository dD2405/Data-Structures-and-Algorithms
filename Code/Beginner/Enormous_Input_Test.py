n,k = map(int,input().split())
c = 0 
for i in range(n):
    t = int(input())

    if(t%k==0):
        c +=1
print(c)

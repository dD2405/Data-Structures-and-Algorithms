a,b = map(int,input().split())
x=abs(a-b)
if x%10==9:
    print(x-1)
else:
    print(x+1) 

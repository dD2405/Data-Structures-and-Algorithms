from fractions import gcd

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    r = a[0]
    for j in a[1:]:
        r = gcd(r,j)
    if(r == 1):
        print(0)
    else:
        print(-1)

#This problem is unsolved as of now any changes and help is appreciated

t = int(input())
l = []

for i in range(t):
    N,minx,maxx = map(int,input().split())
    for i in range(N):
        w1,b1 = map(int,input().split())
        w2,b2 = map(int,input().split())
        for x in range(maxx+1):
            y = w1*x + b1
            print(y,'----')
            z = w2*y + b2
            print(z)

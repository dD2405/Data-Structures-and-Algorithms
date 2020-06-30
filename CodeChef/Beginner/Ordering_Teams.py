t = int(input())

for i in range(t):

    p1 = list(map(int,input().split()))
    p1 = sum(p1)

    p2 = list(map(int,input().split()))
    p2 = sum(p2)

    p3 = list(map(int,input().split()))
    p3 = sum(p3)

    if(p3==p2 or p3==p1):
        print("no")

    elif((p1>p2 and p2>p3)or(p1>p3 and p3>p2)or(p2>p1 and p1>p3)or(p2>p3 and p3>p1)or(p3>p2 and p2>p1)or(p3>p1 and p1>p2)):
        print("yes")
        

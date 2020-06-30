t = int(input())

for i in range(t):
    x1,x2,x3,v1,v2 = map(int,input().split())

    T1 = (abs(x3-x1))/v1
    T2 = (abs(x3-x2))/v2

    if(T1>T2):
        print("Kefa")

    elif(T1==T2):
        print("Draw")

    else:
        print("Chef")

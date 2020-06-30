t=int(input())

for case in range(t):
    X,Y,K,N=map(int,input().split())
    Z=X-Y
    flag=0

    for i in range(N):
        P,C=map(int,input().split())

        if(C<=K and Z<=P):
            flag=1

    if flag==1:
        print('LuckyChef')
    else:
        print('UnluckyChef')

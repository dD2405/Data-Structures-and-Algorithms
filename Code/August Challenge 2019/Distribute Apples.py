t = int(input())

for i in range(t):
    n,k = map(int,input().split())

    if(k==1):
        print("NO")

    elif(n%(k*k)==0):
        print("NO")

    else:
        print("YES")

t=int(input())
for z in range(0,t):
    n=int(input())
    s=input()
    count=0
    for i in range(0,n):
        if s[i]=='1':
            count+=1
    print(int((count*(count+1))/2))

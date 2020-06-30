n=int(input())
for i in range(n):
    x=input()
    l=len(x)
    r=int(x[0])+int(x[l-1])
    print(r)

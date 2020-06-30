def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

t = int(input())

for i in range(t):
    num = int(input())
    print(fact(num))

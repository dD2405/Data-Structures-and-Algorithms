t = int(input())
li = []

for i in range(t):
    n = int(input())
    li.append(n)

li.sort()

for i in range(len(li)):
    print(li[i])
    

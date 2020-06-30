t = int(input())

score , foul = [],[]
for i in range(t):
    result = []
    n = int(input())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    for ele in a:
        score.append(ele*20)
    for ele in b:
        foul.append(ele*10)

    while score != [] and foul != []:

        res = score.pop() - foul.pop()

        if(res <= 0):
            result.append(0)
        else:
            result.append(res)
        
    print(max(result))



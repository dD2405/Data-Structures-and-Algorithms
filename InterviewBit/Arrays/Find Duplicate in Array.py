def repeatedNumber(li):
    li = sorted(li)
    print(li)
    lis = []
    for i in range(len(li)-1):
        if(li[i]==li[i+1]):
            lis.append(li[i])
    print(lis)
    return min(lis)

l = [3,4,1,4,1]
print(repeatedNumber(l))

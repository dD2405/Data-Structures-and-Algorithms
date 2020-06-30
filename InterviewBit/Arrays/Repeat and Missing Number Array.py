def task(li):
    li = sorted(li)
    lis = []
    for i in range(len(li)-1):
        if(li[i]==li[i+1]):
            lis.append(li[i])
    #li_set = set(li)
    #li = list(li_set)

    return min(lis)

    '''for j in li:
        if((li[j+1]-li[j])>1):
            lis.append(li[j]+1)
    return lis'''

l = [3,4,1,4,1]
#l = sorted(l)
print(task(l))

def diffk(li,k):

    for i in range(len(li)):
        for j in range(len(li)):
            if(li[j]-li[i]==k and i!=j):
                return 1
    return 0

li = [1,2,2,3,4,5]

print(diffk(li,2))
            

def intersect(A, B):
    #tmp = set(B)
        
    #C = [val for val in A if val in tmp]
        
    #return sorted(C)

    res = sorted(list(set(A).intersection(B)))
    return res

A = [1,2,3,3,4,5,6]
B = [2,3,5,4]

print(intersect(A,B))

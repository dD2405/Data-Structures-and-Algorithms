def intersect(A, B):
    tmp = set(B)
    C = [val for val in A if val in tmp]
    return sorted(C)

    #res = sorted(list(set(A).intersection(B)))
    #return res

A = [1,2,4,5,5,7]
B = [2,5,7]

print(intersect(A,B))

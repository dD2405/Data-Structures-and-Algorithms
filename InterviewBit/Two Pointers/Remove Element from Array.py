def remove(A,B):

    A = [ele for ele in A if ele!=B]
    return A

    '''p = 0
    while p < len(A):
        if A[p] == B:
            A.pop(p)
        else:
            p+=1
    return A'''

li = [2,1,4]
print(remove(li,2))

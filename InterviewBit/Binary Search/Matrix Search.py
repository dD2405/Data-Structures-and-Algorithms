def matrix(A,tar):

    n = len(A)
    i = 0
    j = n-1

    while(i<n and j>-1):
        if(tar == A[i][j]):
            return 1
        else:
            if(tar < A[i][j]):
                j -= 1
            else:
                i += 1
            return 0

A = [[2,29,36,41],[4,30,37,45]]
print(matrix(A,30))
        

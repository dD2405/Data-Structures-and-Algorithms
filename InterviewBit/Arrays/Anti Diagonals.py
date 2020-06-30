def Anti_Diagonals(mat):

    res = []
    '''for i in range(len(mat)):
        print(i)
        k = 1
        for j in range(len(mat)):
            print(j)
            if((i == j) and mat[i][j] not in res):
                res.append(mat[i][j])

            elif((j == k and j > 1) and i<len(mat)-1 and mat[i][j] not in res):
                res.append(mat[i][j])
                res.append(mat[i+1][j-1])
                res.append(mat[k][i])
                k += 1

            elif(j==k and mat[i][j] not in res):
                res.append(mat[i][j])
                res.append(mat[k][i])
                k += 1'''
    n = len(mat)
    for i in range(n+n-1):
        print('i:',i)
        for k in range(i+1):
            j = i-k
            print('k:',k,'j:',j)
            try:
                res.append(mat[k][j])
            except:
                continue
    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(len(mat))
print(Anti_Diagonals(mat))
                
                

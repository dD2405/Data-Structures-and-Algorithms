def rotate_matrix(mat):

    # in place transpose
    for i in range(len(mat)):
        print('i:',i)

        for j in range(i+1,len(mat)):

            print('j:',j)

            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

            print(mat[i][j],mat[j][i])

    for i in range(len(mat)):
        mat[i] = list((mat[i]))

    print(mat)

    for i in range(len(mat)):
        mat[i] = list(reversed(mat[i]))

    print(mat)

mat = [[1,2,3],[4,5,6],[7,8,9]]

rotate_matrix(mat)

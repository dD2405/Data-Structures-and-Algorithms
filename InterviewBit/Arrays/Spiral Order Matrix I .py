def spiral(mat):

    m,n = len(mat),len(mat[0])

    i,k,l = 0,0,0

    last_row, last_column = m-1,n-1

    while(k <= last_row and l <= last_column):

        for i in range(l,last_column+1,1):
            print('i:',i)
            print(mat[k][i])
        k += 1

        for i in range(k,last_row+1,1):
            print(i)
            print(mat[i][last_column])
        last_column -= 1

        if(k <= last_row):
            for i in range(last_column,l-1,-1):
                print('i:',i)
                print(mat[last_row][i])
            last_row -= 1

        if(l <= last_column):
            for i in range(last_row,k-1,-1):
                print('i:',i)
                print(mat[i][l])
            l += 1

mat = [[1,2,3],[4,5,6],[7,8,9]]
spiral(mat)

        

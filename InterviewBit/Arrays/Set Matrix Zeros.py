def setZeroes(arr):
    c=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i][j]==0):
                for k in range(len(arr)):
                    if(c<len(arr)):
                        arr[i][k]=0
                        arr[c][j]=0
                        c+=1
    return arr


mat = [[0,0],[1,1]]

print(setZeroes(mat))

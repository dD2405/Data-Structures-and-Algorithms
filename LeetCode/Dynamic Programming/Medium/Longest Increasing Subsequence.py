def LIS(A):

    length = [1]*len(A)

    for i in range(1,len(A)):
        for j in range(i):
            if(A[j] < A[i]):
                length[i] = max(length[j]+1,length[i])

    print(length)

    return max(length)

A = [4,5,2,1]

print(LIS(A))

def Rearrange_Array(A):

    n = len(A)

    for i in range(n):
        print('i:',i)
        A[i] = A[i] + (A[A[i]]%n)*n
        print('A[i]:',A[i])

    print(A)

    for i in range(n):
        A[i] = A[i]//n
        print('2nd A[i]:',A[i])

    return A

A = [4,0,2,1,3]
print(Rearrange_Array(A))

def wave(A):
    A = sorted(A)

    for i in range(0, len(A)-1, 2):
        A[i], A[i+1] = A[i+1], A[i]
    return A

A = [3,1,2,10,4]

print(wave(A))

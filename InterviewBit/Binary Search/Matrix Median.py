'''def matrix_median(A):

    a = []
    k=0

    for i in range(len(A)):
        for j in range(len(A[0])):
            a.append(A[i][j])

    a = sorted(a)
    n = len(a)

    if(n%2==0):
        low,high = 0,n-1
        mid = (low+high)//2
        med = (a[mid]+a[mid+1])/2
        return med
    
    else:
        low,high = 0,n-1
        mid = (low+high)//2
        return a[mid]'''

import numpy as np
def matrix_median(A):
    A = np.array(A)
    A = A.flatten()
    A = sorted(A)
    n = len(A)

    if(n%2==0):
        low,high = 0,n-1
        mid = (low+high)//2
        med = (A[mid]+A[mid+1])/2
        return med
    
    else:
        low,high = 0,n-1
        mid = (low+high)//2
        return A[mid]


A = [[1,3,5],[2,6,9],[3,6,9]]

print(matrix_median(A))
    

import time
start = time.time()
def median(A,B):

    A = sorted(A+B)
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

A = [10,20,30]
B = []
print(median(A,B))
end = time.time()

print(end-start)

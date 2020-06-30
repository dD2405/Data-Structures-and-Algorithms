import bisect
def insert(A,tar):

    n = len(A)
    low,high = 0,n-1

    while(low <= high):
        mid = (low+high)//2

        if(A[mid]==tar):
            return mid

        elif(tar > A[mid]):
            low = mid+1
        else:
            high = mid-1

    if tar not in A:
        bisect.insort(A,tar)
        #A.append(tar)
        #A.sort()
        return A.index(tar)
       

A = [1,3,5,6,9,12,15,57,78,100,101]
print(insert(A,10))

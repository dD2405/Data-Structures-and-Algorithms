def rotate(A):

    n = len(A)
    low = 0
    high = n-1
    
    while(low <= high):
        if(A[low]<=A[high]):
            print(A[low],A[high])
            return A[low]

        mid = (low+high)//2
        print('mid:',mid)
        next_pos = (mid+1)%n
        print('next_pos:',next_pos)
        prev_pos = (mid+n-1)%n
        print('prev_pos:',prev_pos)

        if(A[mid]<=A[next_pos] and A[mid]<=A[prev_pos]):
            return A[mid]

        elif(A[mid]<=A[high]):
            high = mid-1

        elif(A[mid]>=A[low]):
            low = mid+1

    return -1

li = [4,5,6,7,0,1,2]
print(rotate(li))

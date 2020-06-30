def gap(A):

    A = sorted(A)
    print(A)
    diff,max_value = 0,0
    for i in range(len(A)-1):

        diff = A[i+1]-A[i]
        if(diff>max_value):
            max_value = diff

    return max_value


A = [1,11,5,7,2]

print(gap(A))
            

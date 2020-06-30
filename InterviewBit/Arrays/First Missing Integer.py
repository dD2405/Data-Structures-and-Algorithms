def firstMissingPositive(A):
    m = max(A) #Storing maximum value 

    if m < 1:
        return 1 

    if len(A) == 1:
        return 2 if A[0] == 1 else 1     
    
    l = [0] * m
    print(l)

    for i in range(len(A)):
        print('i:',i)
        if A[i] > 0:
            print('A[i]',A[i])
            if l[A[i] - 1] != 1:
                l[A[i] - 1] = 1
                print(l)
        
    for i in range(len(l)):
        if l[i] == 0:  
            return i+1

    return i+2     

A = [3,1,5,2]

print(firstMissingPositive(A))

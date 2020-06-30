def maxSubArray(A):
    local_max = 0
    global_max = -200000
    start = 0
    end,beg = 0,0

    for i in range(len(A)):
        local_max = max(A[i],A[i]+local_max)
        print('local_max:',local_max)

        if(local_max < 0):
            local_max = 0
            beg = i+1
            print(beg)

        if(local_max > global_max):
            global_max = local_max
            start = beg 
            end = i
            print('start, end :', start,end)
            print('global_max:',global_max)

    return global_max,start,end

A = [1,1,0,2,3]

print(maxSubArray(A))

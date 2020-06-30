import time

start = time.time()

# bubble sort
'''def sort_color(li):
    
    for i in range(len(li)):
        swap = False

        for j in range(1,len(li)-i):
            
            if(li[j-1]>li[j]):
                li[j-1],li[j] = li[j],li[j-1]
                swap = True

        if(swap == False):
            break
        else:
            continue

    return li'''

# Counting Sort
def sort_color(li):

    # As range of numbers is 0-2 in the question
    max_val = 2
    
    m = max_val + 1

    # creating an array to count the occurences of the number
    count = [0]*m
    print(count)

    # counting the number of occurences
    for a in li:
        print(a)
        count[a] += 1
        print('count[a]:',count[a])
        
    print(count)

    i = 0
    for a in range(m):
        for c in range(count[a]):
            li[i] = a
            i += 1
    return li

'''def sort_color(li):
    count0,count1 = 0,0

    for i in range(0,len(li)):
        if(li[i]==0):
            count0 += 1
        elif(li[i]==1):
            count1 += 1
    print(count0,count1)

    for i in range(0,count0):
        li[i] = 0

    for i in range(count0,count1):
        li[i] = 1

    for i in range(count1,len(li)):
        li[i] = 2

    return li'''
    

li = [0,2,1,1,2,0,1]

print(sort_color(li))

end = time.time()

print(end-start)

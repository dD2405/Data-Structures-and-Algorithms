'''def Repeat_Number(A):

    from collections import Counter

    count = Counter(A)

    print(count)

    for ele in A:
        #print('iterarion:',ele)
        if(count[ele]>len(A)//3):
            return ele

    return -1'''
            

def Repeat_Number(A):

    m = max(A)+1
    count = [0]*m
    print(count)

    for ele in A:
        count[ele] += 1

    print(count)

A = [2,1,2]
print(Repeat_Number(A))
print(len(A))

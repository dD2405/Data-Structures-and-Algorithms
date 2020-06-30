# partially accepted

def num(A):
    #A = [str(i) for i in A]
    for i in A:
        if(A.count(i)==1):
            break
    return int(i)

print(num([1,2,2,3,1]))

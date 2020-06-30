def plusOne(A):
    A=[str(i) for i in A]
    st=''.join(A)
    st=int(st)+1
    st=[int(x) for x in str(st)]
    st=[str(j) for j in st]
    if(len(st)==1):
        return st[0]
    else:
        return st
li = [1,2,3]
print(plusOne(li))

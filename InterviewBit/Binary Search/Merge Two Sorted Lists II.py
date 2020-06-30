def merge(A, B):
    A = sorted(A+B)
    print(A)
    A = [str(val) for val in A ]
    print (" ".join(A) + " " )

A = [1,5,8]
B = [6,9]

print(merge(A,B))

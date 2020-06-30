def merge(A, B):
    A = sorted(A+B)
    A = [str(val) for val in A ]
    print (" ".join(A) + " " )

A = [2,1,5]
B = [7,2,4]

merge(A,B)

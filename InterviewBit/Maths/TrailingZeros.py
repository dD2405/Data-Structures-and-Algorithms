def trailingZeroes(A):
    TrailingZeroes=0
    i=5

    while(i<A+1):
        TrailingZeroes=TrailingZeroes+int((A/i))
        i*=5

    return TrailingZeroes


print(trailingZeroes(10))

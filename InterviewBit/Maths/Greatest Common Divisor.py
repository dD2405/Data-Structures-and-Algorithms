def gcd(m,n):
    while(m!=n):
        if(m>n):
            if(n==0):
                return m
            else:
                m-=n
        elif(n>m):
            if(m==0):
                return n
            else:
                n-=m
            
    return m


print(gcd(6,9))

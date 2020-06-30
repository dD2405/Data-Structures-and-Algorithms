def power(x,n,d):

    #y = x
    '''for i in range(n-1):
        x = x*y
    x = x%d'''
    if(x<0):
        x = x+d
        return x
    elif((x==0 and n==0) or (x==0 and n>0)):
        return 0
    elif(x>0 and n==0):
        return 1
    elif(n==1):
        return x
    
    else:
        res = x*power(x,n-1,d)
        return res


print(power(-1,2,20))

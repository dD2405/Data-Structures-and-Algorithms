# test case
for i in range(int(input())):

    # taking input n,k as told in the question
    n,k = map(int,input().split())

    # creating a list of size n
    a= list(map(int,input().split()))

    # initializing count
    c=0

    # here we add 10 to every element of the list a
    # and check which one is divisible by 7
    # and increment the count
    for i in range(n):
        if((a[i]+k)%7==0):
            c=c+1
    print(c)        

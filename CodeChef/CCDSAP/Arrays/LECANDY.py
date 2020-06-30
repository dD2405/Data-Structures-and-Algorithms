# No. of test cases
t=int(input())

for i in range(t):
    sum=0
    
    # taking input the no. of elephants and candies
    n,c = map(int,input().split())
    
    # a list to store the distribution of candies
    a = list(map(int,input().split()))
  
    # looping through the no. of elephants
    for i in range(n):
        sum+=a[i]
  
    if(sum<=c):
        print('Yes')
    else:
        print('No')
  

    

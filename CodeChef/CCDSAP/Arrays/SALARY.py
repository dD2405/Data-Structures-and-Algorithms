# No. of test cases
for i in range(int(input())):
  
  # No. of workers
  N = int(input())
  
  # Creating a list of workers according to their salary
  Wi = list(map(int,input().split()))
  
  # Formula to calculate the total no. of steps to equalize salary of workers 
  res = sum(Wi)-N*(min(Wi))
  print(res)
  

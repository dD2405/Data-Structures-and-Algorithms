# Test Case t
for t in range(int(input()):
	  
  	# N denoting the no. of elements 
	N = int(input())
	
  	# Taking input A1,A2,A3,.....
	A = list(map(int,input().split())
  
  	# Checking if the list A satisfies the pallindromic condition
  	# Checking whether the user inputed list has elements within the set 
	if A==A[::-1] and list(set(A))==[1,2,3,4,5,6,7]:
		print("yes")
	else:
		print("no")

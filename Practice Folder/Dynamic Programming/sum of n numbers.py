def nSum(n):
	dp = [0] * (n+1)
    	dp[0] = 0

    	for i in range(1,n+1):
		dp[i] = dp[i-1] + i
		print(dp)

	return  dp[n]

print(nSum(0))

import time

start = time.time()
n = 600851475143
i = 4
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

end  = time.time() - start
print("time taken",end)
print (n)

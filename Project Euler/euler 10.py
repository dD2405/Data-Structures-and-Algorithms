import math
import time

start=time.time()
def check_prime(num):
    if num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, (int(math.sqrt(num))) + 1, 2): #range(start,beyondstep,step)
            if num % i == 0:
                return False
    return True


def find_sum(limit):
    sum = 0
    for i in range(2, limit):
        if check_prime(i):
            sum += i
    
    return sum



    # Find the sum of all primes below two million

print(find_sum(2000000))

    # confirm above is correct by solving example
    # and verifying results are euqal to that presented
    # by example
print(find_sum(10))

end=time.time()-start
print("runtime",end)


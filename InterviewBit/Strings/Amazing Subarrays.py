import time

def Amazing_Subarrays(string):
    
    '''res =[]
    n = len(string)
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(n):
        #print('i:',i)
        for j in range(i+1,n+1):
            #print('j:',j)
            if string[i] in vowels:
                res.append(string[i:j])'''

    ret = 0
    n = len(string)
    i = 0

    for x in string:
        print('x:',x)
        if x in 'aeiouAEIOU':
            print(string[i:])
            ret += len(string[i:])
            print('ret:',ret)
        i += 1
        print('i:',i)

    return ret%10003


string = 'ABEC'
print(Amazing_Subarrays(string)) 

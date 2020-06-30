def pow_of_2(num):

    '''remainder,flag = 0,0

    while(num != 0):

        remainder = num%2
        num = num//2

    if(remainder == 0):
        flag = 1
    else:
        flag = 0

    if(flag==1):
        return flag
    else:
        return flag'''

    result = bin(num)#.replace('0b','')
    count_1s = result.count('1')

    

    if(count_1s == 1):
        return 1
    else:
        return 0

print(pow_of_2(6))

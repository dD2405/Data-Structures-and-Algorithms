'''def remove_duplicates(li):
    for i in range(1,len(li)):
        if(li[i-1]==li[i]):
            li[i] = -1

    print(li)

    new_li = list(filter(lambda x:x>=0,li))
    print(new_li)

    return len(new_li)'''


def remove_duplicates(li):
    if(len(li)==1):
        return sum(li)
    else:
        li = list(dict.fromkeys(li))
        print(li)
        return len(li)

'''def removeDuplicates(nums):
    if len(nums)<2:
        return len(nums)
        
    pre = 0
    for cur in range(1,len(nums)):
        if nums[cur]!=nums[pre]:
            pre+=1
            nums[pre]=nums[cur]

    return pre+1'''

'''def remove_duplicates(li):
    if(len(li)==1):
        return sum(li)
    else:
        i=0
        for elem in li:
            if(elem>li[i]):
                i += 1
                li[i] = elem
        return li'''
                
A = [0,1,1,2,2,3]
print(remove_duplicates(A))

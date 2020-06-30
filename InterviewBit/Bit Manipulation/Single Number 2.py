def singleNumber(nums):
    dic={}
    for i in nums:
        if i not in dic:
            dic[i]=1
            print(dic[i],'not')
        else:
            dic[i]+=1
            print(dic[i])
    print(dic)
    for i in dic:
        print(i)
        if dic[i] == 1:
            print(i,'ans')
            return i
    

li = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
print(singleNumber(li))

def LastWord(s):
    l = s.split()
    print(l)

    if(l!=[]):
        length = len(l[-1])
        return length
    else:
        return 0
        

print(LastWord('hello     dfgdfgkfgkfdkg   kkk'))
    

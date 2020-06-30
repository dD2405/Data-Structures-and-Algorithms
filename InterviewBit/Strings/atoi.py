def atoi(st):
    start_index,end_index = 0,0
    st = list(st)
    
    for ch in range(len(st)):
        if(ord(st[ch])>=48 and ord(st[ch])<=57):
            start_index = ch
            break

    for i in range(start_index,len(st)):

        if(ord(st[i])>=48 and ord(st[i])<=57):
            if(i==len(st)-1):
                end_index+=1
            else:
                continue
        else:
            end_index = i;
            break
    print(start_index,end_index)
    for i in range(start_index,end_index):
        return (st)

print(atoi('12232a'))
        
    

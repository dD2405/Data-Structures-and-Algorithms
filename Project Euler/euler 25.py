a,b = 0,1
c1=0

for i in range(0,5000):
    
    c = a+b
    a=b
    b=c

    s_num = str(c)
    l  = len(s_num)
    c1 = c1 + 1 
   
    if(l ==1000):
        break;
    
    
print(c1)

def fizzBuzz(A):
    li=[]
    for fizzbuzz in range(1,A+1):
        if fizzbuzz%15== 0:
            li.append("FizzBuzz")                                          
       
        elif fizzbuzz % 3 == 0:
            li.append("Fizz")                                          
        
        elif fizzbuzz % 5 == 0:
            li.append("Buzz")                                      
       
        else:
            li.append(str(fizzbuzz))
    return li

A = 5
print(fizzBuzz(A))

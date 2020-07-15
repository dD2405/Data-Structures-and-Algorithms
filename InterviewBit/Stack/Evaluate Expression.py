def evaluate(A):

    stack = []

    operator = ['+', '-', '*' , '/']

    for i in range(len(A)):
        if(A[i] not in operator):
            stack.append(A[i])

        #elif(len(A) == 1):
            
        else:
            op = A[i]
            value1 = stack.pop()
            value2 = stack.pop()

            if(op == '+'):
                value3 = int(value2) + int(value1)
            if(op == '-'):
                value3 = int(value2) - int(value1)
            if(op == '*'):
                value3 = int(value2) * int(value1)
            if(op == '/'):
                value3 = int(value2) // int(value1)

            stack.append(value3)

    res = [int(i) for i in stack]
    return sum(res)

A = ['5','2','+']
print(evaluate(A))
        

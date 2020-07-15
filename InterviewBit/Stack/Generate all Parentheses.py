def parentheses(A):

    stack = list()
    MAP = {")": "(",  "}": "{",  "]": "[", "*":"*"}

    for ele in A:
        if(ele == '*'):
            A = A.replace(ele,'')
        
    for elem in A:
        if elem in ['(', '{', '[','*']:
            stack.append(elem)
            print(stack)
        else:
            print('MAP[elem):',MAP[elem])
            print('top:',stack[-1])
            if not stack or MAP[elem] != stack.pop(-1):
                return 0

    return int(len(stack) == 0)

print(parentheses('{**(**{**[**]})}'))

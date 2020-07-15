def reverse(string):

    stack = []
    for i in string:
        stack.append(i)

    ans = []

    for i in range(len(stack)):
        ans.append(stack.pop())

    ans = ''.join(ans)
    return ans

print(reverse('hello'))

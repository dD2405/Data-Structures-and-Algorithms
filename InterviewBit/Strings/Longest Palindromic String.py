def Palindromic_String(string):

    li = []
    if(len(string)<=1):
        return string
    else:
        for i in string:
            res = ''
            for j in range(1,len(string)):
                if(j==1):
                    res = res+i+string[j]
                else:
                    res = res+string[j]
                    if(res == res[::-1]):
                        li.append(res)
                        print(li)

        return max(li)
            

string = 'abacdfgdcaba'

print(Palindromic_String(string))

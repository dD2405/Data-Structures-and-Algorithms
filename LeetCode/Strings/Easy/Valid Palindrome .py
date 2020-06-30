li = "A man, a plan, a canal: Panama"

li = li.lower()

'''this filters out the special characters and joins only the remaining
alphanumeric characters with no spaces'''
li = ''.join(filter(str.isalnum,li))
print(li)
rev = li[::-1]

if(rev==li):
    print(1)
else:
    print(0)

print(rev)

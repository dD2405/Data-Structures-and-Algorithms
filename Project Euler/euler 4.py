mylist = []

for i in range(100, 999):
    for j in range(100, 999):
        num = i * j
        if str(num) == str(num)[::-1]:
            mylist.append(num)

print(max(mylist))
